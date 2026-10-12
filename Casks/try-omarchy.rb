cask "try-omarchy" do
  version "0.5.1"
  sha256 "03760f542025600ef29f77319c93d7c3640a3b15fcf73bda75b9caa9fcbd9999"

  url "https://github.com/omacom/try-omarchy/releases/download/v#{version}/TryOmarchy.dmg"
  name "Try Omarchy"
  desc "Hardware-accelerated Omarchy Linux desktop for Apple Silicon Macs"
  homepage "https://github.com/omacom/try-omarchy"

  depends_on arch: :arm64
  depends_on macos: :sequoia

  app "Try Omarchy.app"
end
