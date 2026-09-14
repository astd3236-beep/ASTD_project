# External Data Fetch Flow

## Overview

External financial data enters the system through an integration adapter.

## Flow

External Source
→ Integration Adapter
→ Fetch Raw Data
→ Normalize Transactions
→ AI / Backend Service
→ Store / Process Transactions

## Responsibilities

### Integration Adapter
- Connect to the external source.
- Fetch raw financial transactions.
- Handle provider-specific response formats.

### Normalization
- Convert provider-specific data into the common transaction format.
- Standardize fields such as date, amount, merchant, description, currency, and account.

### AI / Backend
- Receive normalized transactions.
- AI services can categorize, score, detect anomalies, or suggest matches.
- Backend remains authoritative for accounting rules and final records.

## Principle

AI provides suggestions and predictions.
Deterministic accounting rules and user approval remain authoritative.