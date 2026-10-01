"""Update the cask from GitHub release metadata; never download or execute the app."""

import json
import os
from pathlib import Path
import re
import sys


def update(text, release):
    tag = release["tag_name"]
    if not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", tag):
        raise ValueError("Expected a stable vMAJOR.MINOR.PATCH release")
    if release.get("draft") or release.get("prerelease"):
        raise ValueError("Draft and prerelease updates are unsupported")
    assets = [a for a in release["assets"] if a["name"] == "TryOmarchy.dmg"]
    if len(assets) != 1:
        raise ValueError("Expected exactly one TryOmarchy.dmg asset")
    asset = assets[0]
    expected_url = f"https://github.com/omacom/try-omarchy/releases/download/{tag}/TryOmarchy.dmg"
    if asset["browser_download_url"] != expected_url:
        raise ValueError("Unexpected release asset URL")
    digest = asset.get("digest") or ""
    if not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
        raise ValueError("The release asset must provide a SHA-256 digest")
    versions = re.findall(r'^  version "([0-9]+\.[0-9]+\.[0-9]+)"$', text, re.M)
    hashes = re.findall(r'^  sha256 "([0-9a-f]{64})"$', text, re.M)
    if len(versions) != 1 or len(hashes) != 1:
        raise ValueError("Unexpected cask format")
    version = tag[1:]
    if version == versions[0] and digest[7:] != hashes[0]:
        raise ValueError("An existing release's checksum changed; review manually")
    if tuple(map(int, version.split("."))) <= tuple(map(int, versions[0].split("."))):
        return text, None
    text = re.sub(r'^  version ".*"$', f'  version "{version}"', text, flags=re.M)
    text = re.sub(r'^  sha256 ".*"$', f'  sha256 "{digest[7:]}"', text, flags=re.M)
    return text, version


def self_test():
    text = '  version "0.4.1"\n  sha256 "' + "a" * 64 + '"\n'
    release = {"tag_name": "v0.4.2", "assets": [{
        "name": "TryOmarchy.dmg", "digest": "sha256:" + "b" * 64,
        "browser_download_url": "https://github.com/omacom/try-omarchy/releases/download/v0.4.2/TryOmarchy.dmg",
    }]}
    result, version = update(text, release)
    assert version == "0.4.2" and 'version "0.4.2"' in result and "b" * 64 in result
    assert update(result, release) == (result, None)
    for change in ({"tag_name": "v0.4.2; echo bad"}, {"assets": []}, {"prerelease": True}):
        try:
            update(text, release | change)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid release metadata was accepted")
    for digest in (None, "sha256:" + "c" * 64):
        altered = release | {"assets": [release["assets"][0] | {"digest": digest}]}
        try:
            update(result, altered)
        except ValueError:
            pass
        else:
            raise AssertionError("Missing or changed checksum was accepted")
    print("Updater self-checks passed")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        self_test()
    else:
        cask = Path(__file__).resolve().parents[1] / "Casks/try-omarchy.rb"
        text, version = update(cask.read_text(), json.loads(Path(sys.argv[1]).read_text()))
        if version:
            cask.write_text(text)
            with open(os.environ["GITHUB_OUTPUT"], "a") as output:
                output.write(f"version={version}\n")
            print(f"Prepared Try Omarchy {version}")
        else:
            print("Try Omarchy is already up to date")
