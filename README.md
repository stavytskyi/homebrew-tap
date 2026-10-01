# Personal Homebrew tap

Homebrew casks maintained by [stavytskyi](https://github.com/stavytskyi).
This tap is independent of the upstream application authors.

## Try Omarchy

Install the official Apple Silicon app (macOS 15 or newer):

```sh
brew install --cask stavytskyi/tap/try-omarchy
```

Update after a new version has been added to this tap:

```sh
brew update
brew upgrade --cask stavytskyi/tap/try-omarchy
```

Quit Try Omarchy and shut down its guest before upgrading. Back up important VM
data first. If a manually installed app already exists, Homebrew may refuse to
overwrite it. Move only `/Applications/Try Omarchy.app` aside before installing
through Homebrew; keep the old app until the new one has been verified.

The cask uses the upstream release DMG and a fixed SHA-256 checksum. It does not
build Linux or QEMU, update packages inside the guest, or delete VM data. The
existing VM is stored separately under
`~/Library/Application Support/Try Omarchy/VM/v1`.

Uninstall only the Mac app:

```sh
brew uninstall --cask stavytskyi/tap/try-omarchy
```

## Maintenance

GitHub Actions checks the latest stable upstream release every Monday at 07:23
UTC. A newer release is committed directly to `main` only after all checks pass:

- Stable version, expected asset URL, and SHA-256 release metadata.
- Updater self-checks, Homebrew style and strict cask audit.
- Actual DMG download and checksum verification by Homebrew.
- Installation on a disposable Apple Silicon macOS 15 runner.
- Application signature verification and Gatekeeper assessment.
- Existing VM disk and boot-file test fixtures survive installation and uninstall.

No pull-request review or personal token is required. The workflow uses the
repository-scoped `GITHUB_TOKEN`. A failed check prevents publication; GitHub
Actions failure notifications follow your account notification settings.

The checks do not boot Linux or prove that guest package updates work. Real VM
compatibility remains an upstream responsibility. Your Mac is not accessed:
run `brew update` and `brew upgrade` to install the published version locally.

Use **Actions → Update Try Omarchy → Run workflow** to run the checks manually,
even when the version has not changed. This does not create a redundant commit.
Standard GitHub-hosted runners are free for public repositories. No artifacts or
caches are uploaded. GitHub may disable schedules after 60 days without
repository activity; re-enable the workflow from Actions if necessary.

Run the updater's local checks with:

```sh
python3 scripts/update-try-omarchy.py --self-test
```

For a manual update, or when release metadata lacks a SHA-256 digest:

For each upstream release:

1. Review the [release notes](https://github.com/omacom/try-omarchy/releases).
2. Update `version` and `sha256` in `Casks/try-omarchy.rb`; verify the downloaded
   DMG's checksum against the release asset digest.
3. Run `brew style Casks/try-omarchy.rb` and audit the cask in the local tap with
   `brew audit --cask --strict stavytskyi/tap/try-omarchy`.
4. Test installation or upgrade on a Mac with a backed-up VM before publishing.
5. Commit the recipe change and push it. `brew update` picks up the new recipe;
   `brew upgrade` installs it.

Keep app downloads, VM disks, credentials, and personal configuration out of this
repository. No VM removal or `zap` stanza is included.
