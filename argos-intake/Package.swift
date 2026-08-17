// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "ArgosCore",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .library(name: "ArgosCore", targets: ["ArgosCore"])
    ],
    dependencies: [
        // Pure-Swift/cross-platform SHA-256. On Apple platforms `import Crypto`
        // transparently re-exports CryptoKit, so this is the same primitive
        // CLAUDE.md's CryptoKit requirement calls for — it also lets the
        // hashing logic be unit-tested outside Xcode.
        .package(url: "https://github.com/apple/swift-crypto.git", "2.0.0"..<"4.0.0")
    ],
    targets: [
        .target(
            name: "ArgosCore",
            dependencies: [
                .product(name: "Crypto", package: "swift-crypto")
            ]
        ),
        .testTarget(
            name: "ArgosCoreTests",
            dependencies: ["ArgosCore"]
        )
    ]
)
