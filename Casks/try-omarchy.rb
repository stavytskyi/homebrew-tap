cask "try-omarchy" do
  version "1.1.0"
  sha256 "85569dae25d22a2c070bceb5da48d53a5cf593f2e53f1c9d9f9dfeb117258e24"

  url "https://github.com/omacom/try-omarchy/releases/download/v#{version}/TryOmarchy.dmg"
  name "Try Omarchy"
  desc "Hardware-accelerated Omarchy Linux desktop for Apple Silicon Macs"
  homepage "https://github.com/omacom/try-omarchy"

  depends_on arch: :arm64
  depends_on macos: :sequoia

  app "Try Omarchy.app"
end
