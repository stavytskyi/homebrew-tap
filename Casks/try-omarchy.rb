cask "try-omarchy" do
  version "1.2.0"
  sha256 "403e7695c824dc67448d9f273bd105c6a17db2e89fd120d9fc7df1d647af30ba"

  url "https://github.com/omacom/try-omarchy/releases/download/v#{version}/TryOmarchy.dmg"
  name "Try Omarchy"
  desc "Hardware-accelerated Omarchy Linux desktop for Apple Silicon Macs"
  homepage "https://github.com/omacom/try-omarchy"

  depends_on arch: :arm64
  depends_on macos: :sequoia

  app "Try Omarchy.app"
end
