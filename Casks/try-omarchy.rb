cask "try-omarchy" do
  version "0.4.1"
  sha256 "e2f172f67e5d8a99df8e46fa6f7814a061c0af249f100a6bdc7836b922f47674"

  url "https://github.com/omacom/try-omarchy/releases/download/v#{version}/TryOmarchy.dmg"
  name "Try Omarchy"
  desc "Hardware-accelerated Omarchy Linux desktop for Apple Silicon Macs"
  homepage "https://github.com/omacom/try-omarchy"

  depends_on arch: :arm64
  depends_on macos: :sequoia

  app "Try Omarchy.app"
end
