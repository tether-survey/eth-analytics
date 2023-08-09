ZEPPELIN_CONTRACTS = {
    # ACCESS CONTROL
    "Ownable",
    "IAccessControl",
    "AccessControl",
    "AccessControlCrossChain",
    "IAccessControlEnumerable",
    "AccessControlEnumerable",

    # COMMON (TOKENS)
    "ERC2981",

    # CROSS CHAIN AWARENESS
    # CrossChainEnabled specializations
    "CrossChainEnabledAMB",
    "CrossChainEnabledArbitrumL1",
    "CrossChainEnabledArbitrumL2",
    "CrossChainEnabledOptimism",
    "CrossChainEnabledPolygonChild",
    # Libraries for cross-chain
    "LibAMB",
    "LibArbitrumL1",
    "LibArbitrumL2",
    "LibOptimism",


    # ERC 20
    # Core
    "IERC20",
    "IERC20Metadata",
    "ERC20",
    # Extensions
    "ERC20Burnable",
    "ERC20Capped",
    "ERC20Pausable",
    "ERC20Snapshot",
    "ERC20Votes",
    "ERC20VotesComp",
    "ERC20Wrapper",
    "ERC20FlashMint",
    "ERC4626",
    # Draft EIPs
    "ERC20Permit",
    # Presets
    # Utilities
    "SafeERC20",
    "TokenTimelock",

    # ERC 721
    # Core
    "IERC721",
    "IERC721Metadata",
    "IERC721Enumerable",
    "ERC721",
    "ERC721Enumerable",
    "IERC721Receiver",
    # Extensions
    "ERC721Pausable",
    "ERC721Burnable",
    "ERC721URIStorage",
    "ERC721Votes",
    "ERC721Royalty",
    # Presets
    # Utilities

    # ERC721Holder
    # Core
    "IERC777",
    "ERC777",
    # Hooks
    "IERC777Sender",
    "IERC777Recipient",
    # Presets
    "ERC777PresetFixedSupply",

    #     ERC 1155
    # Core
    "IERC1155",
    "IERC1155MetadataURI",
    "ERC1155",
    "IERC1155Receiver",
    "ERC1155Receiver",
    # Extensions
    "ERC1155Pausable",
    "ERC1155Burnable",
    "ERC1155Supply",
    "ERC1155URIStorage",
    # Presets
    # Utilities
    "ERC1155Holder",

    # Contracts
    "PaymentSplitter",
    "VestingWallet",

    # GOVERNANCE
    # Governor
    "Core",
    "IGovernor",
    "Governor",
    "Modules",
    "GovernorCountingSimple",
    "GovernorVotes",
    "GovernorVotesQuorumFraction",
    "GovernorVotesComp",
    "Extensions",
    "GovernorTimelockControl",
    "GovernorTimelockCompound",
    "GovernorSettings",
    "GovernorPreventLateQuorum",
    "GovernorCompatibilityBravo",
    "Deprecated",
    "GovernorProposalThreshold",
    # Utils
    "Votes",
    # Timelock
    "TimelockController",

    #     INTERFACES
    # List of standardized interfaces
    # Detailed ABI
    "IERC1271",
    "IERC1363",
    "IERC1363Receiver",
    "IERC2612",
    "IERC2981",
    "IERC3156FlashLender",
    "IERC3156FlashBorrower",

    # META TRANSACTIONS

    # Core
    "ERC2771Context",
    # Utils
    "MinimalForwarder",


    # PROXIES
    # Transparent vs UUPS Proxies
    # Core
    "Proxy",
    # ERC1967
    "ERC1967Proxy",
    "ERC1967Upgrade",
    # Transparent Proxy
    "TransparentUpgradeableProxy",
    "ProxyAdmin",
    # Beacon
    "BeaconProxy",
    "IBeacon",
    "UpgradeableBeacon",
    # Minimal Clones
    "Clones",
    # Utils
    "Initializable",
    "UUPSUpgradeable",

    # SECURITY
    # Contracts
    "PullPayment",
    "ReentrancyGuard",
    "Pausable ",

    # UTILITIES
    # Math
    "Math",
    "SignedMath",
    "SafeCast",
    "SafeMath",
    "SignedSafeMath",
    # Cryptography
    "ECDSA",
    "SignatureChecker",
    "MerkleProof",
    "EIP712",
    # Escrow
    "ConditionalEscrow",
    "Escrow",
    "RefundEscrow",
    # Introspection
    "IERC165",
    "ERC165",
    "ERC165Storage",
    "ERC165Checker",
    "IERC1820Registry",
    "IERC1820Implementer",
    "ERC1820Implementer",
    # Data Structures
    "BitMaps",
    "EnumerableMap",
    "EnumerableSet",
    "DoubleEndedQueue",
    "Checkpoints",
    # Libraries
    "Create2",
    "Address",
    "Arrays",
    "Base64",
    "Counters",
    "Strings",
    "StorageSlot",
    "Multicall",
}