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
