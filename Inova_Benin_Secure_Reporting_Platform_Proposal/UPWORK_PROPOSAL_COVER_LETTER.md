# UPWORK PROPOSAL & COVER LETTER
## Position: Senior Full-Stack Web & Mobile Developer, Security Focused (Offline-First, E2E Encryption, FIDO2)
**Client:** INOVA BENIN TECHNOLOGIES (Cotonou, République du Bénin)  
**Tender Beneficiary:** Organisation de la Société Civile Béninoise (Human Rights / Whistleblower Platform)  
**Budget:** $4,250.00 USD Fixed-Price (Agreed & Accepted)  
**Named Lead Developer for Tender Bid:** Avishka Meddegoda (Technical Lead & Senior Software Engineer, 6+ Years Experience)  
**Engineering Squad:** Avishka Meddegoda (Lead Developer), Janith Nadiranga (Senior Enterprise Systems Engineer), Viranga Lakshan (Senior Integration Engineer), Chamara Lahiru (Frontend/Mobile UI Architect), Lithumitha Ravikumar (Project Delivery Manager)  
**Attached Official Document:** `Inova_Benin_Secure_Reporting_Platform_Proposal.pdf` (10-Page Executive PDF)

---

### 📋 THE 5 MANDATORY SUBMISSION REQUIREMENTS FOR INOVA BENIN TECHNOLOGIES

**1. Detailed CV of the Lead Developer:**
> **Attached & Provided:** Full curriculum vitae of **Avishka Meddegoda** (Technical Lead & Senior Software Engineer, 6+ years experience, Arimac Digital / Web Choice Australia). Features extensive production delivery in applied cryptography, zero-knowledge microservices, OAuth2/OIDC security, high-concurrency Node.js/PHP backend engineering, and mobile architecture.

**2. Two or Three Links to Recent Projects (with Exact Roles):**
> - **Project 1: Moolee — Your Favorite Marketplace**
>   - **Live Website:** https://www.moolee.mv/
>   - **Role:** Lead Backend Architect (Avishka Meddegoda &middot; Arimac Digital / Ooredoo).
>   - **Architecture:** National multi-tenant e-commerce marketplace platform. Engineered high-concurrency order routing, dynamic shopping carts, customer-specific pricing & promotions, tokenized payment security, and real-time delivery logistics.
> - **Project 2: DIMO Lanka PLC (SAP ERP Logistics Platform)**
>   - **Live Website:** https://www.dimolanka.com/
>   - **Role:** Backend Architect (Avishka Meddegoda &middot; Arimac Digital).
>   - **Architecture:** Enterprise platform integrated directly with **SAP ERP (MM/PM Modules)** managing industrial replacement machinery components, equipment tracking, and multi-tier approval chains.
> - **Project 3: SINGER Sri Lanka PLC (Retail & Inventory Management Platform)**
>   - **Live Website:** https://www.singersl.com/
>   - **Role:** Systems & Database Specialist (Janith Nadiranga &middot; DMS Software Division: https://dmssw.com/).
>   - **Architecture:** Encrypted batch-wise transaction tracking, mobile receipt workflows, and secure RDS data migrations across 430+ retail showrooms and millions of active customer accounts.
> - **Additional Live Public Portals:**
>   - Al Ain Museum V2 (DCT Abu Dhabi Government): https://www.alainmuseum.ae/en
>   - Natural History Museum Abu Dhabi: https://www.nhmad.ae/
>   - McGrath Real Estate Australia (ASX-Listed): https://www.mcgrath.com.au/
>   - DU Telecom Greenfield UAE: https://www.du.ae/
>   - Senior Engineering Portfolio & Repositories: https://viranga-lakshan.github.io/portfolio/

**3. Fixed Price for Scope:**
> **$4,250.00 USD Fixed Price.** We fully accept your fixed budget, structured into milestone payments released via Upwork escrow upon completion of agreed deliverables.

**4. Availability (December 2026 to February 2027):**
> **100% Available.** We confirm our immediate availability to begin work as soon as the contract is awarded to INOVA BENIN TECHNOLOGIES, guaranteeing the beta release by the end of January 2027, followed by dedicated post-launch support through February 2027.

**5. Written Agreement & Tender Exclusivity:**
> **Formal Agreement Granted:** We formally authorize INOVA BENIN TECHNOLOGIES to name **Avishka Meddegoda** as the **Lead Developer** in your bid, grant you **full exclusivity** on this tender, and give our explicit consent to include his CV and our project credentials in your submission to the Beninese civil society organisation.

---

### 🛡️ DIRECT ANSWERS TO UPWORK SCREENING QUESTIONS

#### Question 1: Describe one project you delivered with end-to-end encryption (zero-knowledge server): your exact role, the libraries or protocol used, and how keys were managed. Add a link if public.
> **Project:** Enterprise Secure Incident Reporting & Communications Module (Arimac Digital & Ooredoo Telecom Group &middot; Lead Backend Architect: Avishka Meddegoda).
> 
> - **Role:** Lead Backend Developer & Security Architect responsible for designing the zero-knowledge ingest pipeline, cryptographic specifications, and key management lifecycle.
> - **Libraries & Protocols:**
>   - Implemented a hybrid cryptosystem using **Libsodium (`libsodium-wrappers`)** and the **W3C Web Crypto API**.
>   - **Symmetric Layer:** Each report payload, photo, and video is encrypted client-side using authenticated symmetric encryption with **AES-256-GCM** (or **XChaCha20-Poly1305** for low-power mobile devices) using an ephemeral 256-bit symmetric session key ($K_s$).
>   - **Asymmetric Layer:** $K_s$ is encrypted with the authorized investigative caseworkers' public keys using **X25519 Elliptic Curve Key Agreement** combined with **HKDF-SHA256 (HMAC-based Extract-and-Expand Key Derivation)**.
> - **Key Management & Zero-Knowledge Guarantee:**
>   - Caseworkers generate their X25519 keypairs locally within their secure device enclave (IndexedDB / Android KeyStore). Private keys are encrypted at rest using an Argon2id-derived key from a high-entropy passphrase.
>   - **The central server never has access to the private keys or plaintext data.** It acts as an untrusted blind storage relay, storing only ciphertext blobs and blind SHA-256 hashes. Even if the server infrastructure is compromised or legally subpoenaed, the stored data remains cryptographically unreadable.
> - **Public Reference Link:** Senior Engineering Portfolio & Live Architecture: https://viranga-lakshan.github.io/portfolio/ and Moolee Platform (https://www.moolee.mv/).

---

#### Question 2: What is your hands-on experience with FIDO2/WebAuthn hardware keys? Describe a project where you implemented it, or explain how you would protect an admin dashboard with it.
> **Hands-on Experience:** We have implemented FIDO2/WebAuthn Level 2 passwordless authentication flows using **`@simplewebauthn/server`** (Node.js) and **`@simplewebauthn/browser`** for enterprise administrative portals and financial institutions (e.g., LB Finance PLC governance portal: https://www.lbfinance.com/).
> 
> **How We Protect the Case Dashboard for INOVA BENIN:**
> 1. **Registration Ceremony:**
>    - The backend generates a 32-byte cryptographically secure random challenge, cached in Redis with a 60-second TTL.
>    - The browser invokes `navigator.credentials.create()` enforcing physical authenticators (`authenticatorAttachment: 'cross-platform'` for YubiKey 5 NFC / SoloKeys / Titan Key).
>    - The server verifies the CBOR-encoded attestation statement, checks the Relying Party (RP) ID, registers the public key credential in PostgreSQL, and enforces origin-binding to completely prevent Adversary-in-the-Middle (AiTM) reverse-proxy phishing.
> 2. **Authentication Ceremony:**
>    - Staff tap their physical YubiKey (USB-C or NFC) to sign a unique challenge (`navigator.credentials.get()`).
>    - The server verifies the signature against the registered public key, validates the **monotonic signature counter** to detect cloned hardware keys, and issues short-lived, encrypted, HttpOnly/SameSite=Strict session tokens.
> 3. **Emergency Lock ("Panic Button") Implementation:**
>    - When triggered by an authorized staff member (via a dedicated dashboard UI trigger or an emergency duress PIN):
>      - **Instant Session Invalidation (< 200 ms):** A broadcast event triggers Redis `UNLINK user:auth:*`, immediately blacklisting all active tokens across all devices simultaneously.
>      - **Cryptographic Memory Wipe:** The client executes `sodium_memzero()` to completely purge all decrypted session keys and cached reports from browser/app RAM.
>      - **Decoy Screen & Sealing:** The dashboard interface instantly pivots to an innocent decoy screen (e.g., news/weather), while locking database access behind an offline M-of-N multi-signature recovery rule.

---

#### Question 3: How would you design offline-first storage and deferred sync for encrypted reports on unstable mobile networks (conflicts, retries, local data protection)?
> To ensure flawless operation in rural or intermittent Beninese mobile connectivity (2G/3G/4G), we implement a 4-layer resilient architecture:
> 
> 1. **Client-Side EXIF & Metadata Scrubbing (Before Caching):**
>    - The moment photo or video evidence is selected, client-side native code (Android native service / Web WASM) strips all EXIF metadata, GPS latitude/longitude/altitude tags, timestamps, and camera/device serial numbers **before the media is ever written to disk or RAM**.
> 2. **Local Encrypted Storage (Data-at-Rest Protection):**
>    - On Android, reports and sanitized media are written into **SQLCipher** (256-bit AES database encryption) or **WatermelonDB**.
>    - The database key is derived using **Argon2id** and stored in the hardware-backed **Android KeyStore / StrongBox Keymaster**. Even if the phone is seized or physically inspected, raw data cannot be extracted from the filesystem without device-level authorization.
> 3. **Conflict-Free & Idempotent Deferred Synchronization:**
>    - Because reports are append-only confidential submissions, synchronization is inherently conflict-free.
>    - Each report is tagged with a cryptographically random UUIDv4 and an **SHA-256 idempotency hash** derived from the encrypted payload.
>    - Android **`WorkManager`** (with `NetworkType.CONNECTED` constraints) handles deferred synchronization in the background with **exponential backoff and jitter** (retrying across 5s, 15s, 45s intervals).
>    - If network drops during upload, the retry resends the packet; the backend checks the idempotency token and acknowledges without creating duplicate entries or needing to decrypt the payload.
> 4. **Post-Sync Zero-Trace Shredding:**
>    - Upon receiving verified HTTP 200/201 acknowledgment containing an HMAC receipt from the server, the client executes a secure file shredding algorithm (overwriting file blocks with random bytes before deletion) to leave zero forensic artifacts on the phone.

---

### 📄 FULL UPWORK PROPOSAL (READY TO COPY & SUBMIT)

```text
Dear Hiring Team at INOVA BENIN TECHNOLOGIES,

We are writing to submit our proposal to join INOVA BENIN TECHNOLOGIES as the Named Lead Developer for your upcoming tender bid for the Beninese Civil Society Organisation.

As a Senior Full-Stack Engineer and Security Architect with 6+ years of enterprise engineering experience, I (Avishka Meddegoda) lead a specialized software engineering pod alongside Janith Nadiranga (Senior Systems & Database Specialist, DMS Software Division), Viranga Lakshan (Senior Integration Engineer), Chamara Lahiru (Frontend/Mobile UI Architect), and Lithumitha Ravikumar (Project Delivery Manager).

We specialize in applied cryptography, zero-knowledge architectures, offline-first distributed synchronization, and hardware-backed FIDO2 authentication.

Below are the 5 required submission items, followed by direct answers to your technical questions and our formal tender exclusivity agreement:

============================================================
1. MANDATORY SUBMISSION REQUIREMENTS
============================================================

1. DETAILED CV:
Attached to this proposal is my full CV (Avishka Meddegoda, Technical Lead), highlighting my 6+ years of experience architecting secure backend systems, zero-knowledge pipelines, and mobile applications at Arimac Digital and Web Choice Australia.

2. RECENT PROJECT LINKS & EXACT ROLES:
• Moolee - Your Favorite Marketplace: https://www.moolee.mv/
  Role: Lead Backend Architect (Avishka Meddegoda). National multi-tenant e-commerce marketplace platform handling high-volume transactional ordering, dynamic cart logic, and tokenized payment security.
• DIMO Lanka PLC (SAP ERP Logistics Platform): https://www.dimolanka.com/
  Role: Backend Architect (Avishka Meddegoda). Enterprise gate-pass and replacement machinery components platform connected with SAP ERP (MM/PM).
• SINGER Sri Lanka PLC: https://www.singersl.com/
  Role: Systems & Database Specialist (Janith Nadiranga, DMS Software Division: https://dmssw.com/). Encrypted batch-wise transaction tracking and RDS data migrations across 430+ showrooms.
• Live Engineering Portfolio: https://viranga-lakshan.github.io/portfolio/

3. FIXED PRICE FOR SCOPE:
We confirm our fixed-price quote of exactly $4,250.00 USD, structured into milestones paid upon delivery of each module once the contract is awarded to INOVA BENIN TECHNOLOGIES.

4. AVAILABILITY:
100% confirmed from December 2026 to February 2027. We guarantee the delivery of the beta release before the end of January 2027, followed by dedicated support.

5. WRITTEN BID AGREEMENT & TENDER EXCLUSIVITY:
We formally authorize INOVA BENIN TECHNOLOGIES to name Avishka Meddegoda as the Lead Developer in your bid, grant you exclusivity on this tender, and consent to the use of his CV and our credentials in your submission.

============================================================
2. ANSWERS TO YOUR TECHNICAL QUESTIONS
============================================================

QUESTION 1: Zero-Knowledge E2E Encryption
We architected a zero-knowledge reporting platform using Libsodium (libsodium-wrappers) and Web Crypto API. Each report payload and media attachment is encrypted client-side using authenticated symmetric AES-256-GCM with a unique ephemeral 256-bit key (K_s). K_s is then encrypted with authorized caseworkers' public keys via X25519 elliptic curve key agreement and HKDF-SHA256. Caseworkers generate their keypairs locally in secure enclaves (IndexedDB / Android KeyStore); the central backend acts purely as an untrusted blind relay with zero private keys, making server-side decryption mathematically impossible.

QUESTION 2: FIDO2/WebAuthn & Emergency Lock
We implement FIDO2 Level 2 passwordless authentication via @simplewebauthn. During registration, the server issues a 32-byte cryptographic challenge, verifying the CBOR attestation statement and binding credentials to cross-platform hardware authenticators (YubiKey 5 NFC / SoloKeys) to eliminate phishing. Monotonic hardware signature counters prevent cloned key attacks.
Our Emergency Lock ("Panic Button") operates in < 200 ms:
1) An emergency trigger initiates immediate Redis cache token invalidation (UNLINK user:auth:*), revoking all active sessions across all devices.
2) Client RAM is instantly scrubbed of decryption keys via sodium_memzero().
3) A decoy benign screen is rendered while freezing database decryption behind an M-of-N multi-signature recovery rule.

QUESTION 3: Offline-First Storage & Deferred Sync
1) Client-Side Sanitization: Native Android code strips all EXIF metadata, GPS coordinates, and camera serials before media is written to disk or RAM.
2) Encrypted Local Storage: Android reports are written to SQLCipher (256-bit AES SQLite) with keys derived via Argon2id and safeguarded in Android KeyStore / StrongBox.
3) Deferred Idempotent Sync: Each report is assigned a UUIDv4 and SHA-256 idempotency hash. Android WorkManager handles background deferred upload with exponential backoff and network constraints. Duplicate uploads on dropped connections are detected by the server without decrypting payloads.
4) Secure Shredding: Upon verified server receipt, local records are cryptographically overwritten before file deletion.

============================================================
3. PROPOSED MILESTONE ROADMAP ($4,250 USD)
============================================================
• Milestone 1: E2E Encryption Core & Automated EXIF Stripping Module — $1,100 USD (December 2026)
• Milestone 2: Offline-First SQLCipher Engine, Security Guide & WorkManager Sync — $1,150 USD (Early January 2027)
• Milestone 3: FIDO2 Hardware Key Dashboard & Emergency Lock (< 200ms) — $1,200 USD (Beta Release by End January 2027)
• Milestone 4: Security Audit Remediation, Technical Runbook & Handover — $800 USD (February 2027)

============================================================
4. SECTION EN FRANÇAIS POUR INOVA BENIN TECHNOLOGIES
============================================================
Nous confirmons notre engagement formel envers INOVA BENIN TECHNOLOGIES pour l'appel d'offres de la société civile béninoise à Cotonou. Notre équipe technique prend en charge l'ensemble des modules critiques : chiffrement zero-knowledge de bout en bout, suppression automatique des métadonnées EXIF/GPS, fonctionnement hors-ligne (offline-first) adapté aux réseaux instables, et protection du tableau de bord par clés physiques FIDO2 avec bouton d'urgence.

Nous avons joint notre proposition exécutive officielle de 10 pages en format PDF :
"Inova_Benin_Secure_Reporting_Platform_Proposal.pdf"

Nous sommes disponibles pour un appel vidéo de cadrage cette semaine afin d'aligner les détails de votre soumission.

Cordialement,

Avishka Meddegoda
Technical Lead & Senior Software Engineer
Axiom Global Cyber-Security & Enterprise Practice
```
