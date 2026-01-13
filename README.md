# 🚗 CarCANex — CAN Explorer & eXchange

<p align="center">
  <img src="assets/logo.png" alt="CarCANex Logo" width="200">
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+"></a>
  <a href="https://www.rust-lang.org/"><img src="https://img.shields.io/badge/rust-stable-orange.svg" alt="Rust"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
</p>

---

**CarCANex** is a modern, high-performance, and scalable CAN bus exploration and exchange SDK. Engineered for both automotive researchers and professional engineers, it bridges the gap between raw vehicle data and actionable insights using a high-performance **Python + Rust hybrid architecture**.

## 🧠 Core Philosophy

CarCANex is built on three pillars:

*   **🔍 Explorer**: Real-time signal decoding, time-series analysis, and dependency mapping.
*   **🔄 eXchange**: Seamless data bridging between diverse vehicle interfaces and analysis tools.
*   **🛡️ Security**: Integrated functional safety logic (MISRA-inspired) and runtime validation.

## 🧱 Key Features

| Feature | Description |
| :--- | :--- |
| **Hybrid Core** | Blazing fast CAN frame parsing in Rust with a flexible Python API. |
| **DBC Suite** | Advanced management, validation, and multi-database decoding. |
| **Universal Car Interface** | Standardized abstraction layer for any vehicle platform. |
| **Safety Validator** | Real-time frequency monitoring and signal limit enforcement. |
| **High-Fi Simulation** | Replay precise CAN traffic with sub-millisecond accuracy. |
| **Premium CLI** | Rich, interactive command-line interface for rapid field analysis. |

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ismailtsdln/CarCANex.git
cd CarCANex

# Install the SDK in editable mode
pip install -e .
```

### Basic Usage (CLI)

#### 📝 Parse Logs
```bash
carcanex parse --dbc model3.dbc --log capture.asc
```

#### 🔍 Real-time Monitor
```bash
carcanex monitor --interface vcan0
```

### Python SDK

```python
from carcanex import CarCANex

# Initialize with vehicle DBC
explorer = CarCANex(dbc_path="tesla_model3.dbc")

# Stream parsed data
for msg in explorer.stream("capture.log"):
    if "SPEED" in msg.decoded:
        print(f"Current Speed: {msg.decoded['SPEED']} km/h")
```

## 🛠️ Architecture

CarCANex leverages a **split-responsibility architecture**:

*   **Rust Layer**: Native performance for bit-level parsing and high-throughput streaming.
*   **Python Layer**: Rich ecosystem integration, rapid prototyping, and advanced analytics.

## 🤝 Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a new vehicle DBC, or improving the documentation, please check out our [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ for the Automotive Community by <a href="https://github.com/ismailtsdln">Ismail Tasdelen</a>
</p>
