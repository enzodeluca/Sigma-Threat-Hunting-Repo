## Detection-as-Code: Sigma Rules

This section contains platform-agnostic detection logic written in the universal **Sigma** standard formatting. These rules are designed to be integrated into CI/CD pipelines and compiled into native SIEM query languages on the fly.

### Rules Available
* **[lnx_ssh_bruteforce.yml](./detections/linux/lnx_ssh_bruteforce.yml)**: Detects high-frequency failed SSH authentication attempts on Linux systems, targeting credential stuffing and brute-force patterns.

### Validation & Compilation Workflow
The rules in this directory are tested and validated using `sigma-cli` and the `pySigma` translation engine. For example, to compile the SSH brute-force rule into native **Splunk SPL** or **SQL data lake** queries without platform pipeline filters, use the following commands:

```bash
# Translate to Splunk Search Processing Language (SPL)
sigma convert --without-pipelines -t splunk lnx_ssh_bruteforce.yml

# Translate to ANSI-compliant SQLite WHERE clauses
sigma convert --without-pipelines -t sqlite lnx_ssh_bruteforce.yml
