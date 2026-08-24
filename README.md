# Large-Scale CSV Batch Processing Pipeline

## Overview

This project demonstrates a batch-processing architecture for
reliably processing large CSV datasets and loading curated data
into Azure SQL Database.

The solution uses Python-based chunk processing to avoid loading
the complete dataset into memory.

## Architecture

Large CSV
   ↓
Azure Blob Storage
   ↓
Python Batch Processor
   ↓
Data Quality Validation
   ↓
Transformation
   ↓
Processed Data
   ↓
Azure SQL
   ↓
Power BI

## Technologies

- Python
- Pandas
- Azure Blob Storage
- Azure SQL Database
- SQL
- Power BI

## Key Features

- Large-file batch processing
- Chunk-based CSV processing
- Data validation
- Duplicate detection
- Invalid-record handling
- Revenue calculation
- Processed data generation
- SQL-based analytics
- Cloud storage architecture

## Batch Processing

The pipeline processes CSV data in configurable chunks rather
than loading the entire file into memory.

This approach improves memory efficiency and provides a foundation
for processing larger datasets.

## Data Quality

The pipeline validates:

- Duplicate order IDs
- Missing order IDs
- Invalid quantities
- Invalid prices
- Missing customer information

## Fault Tolerance

The solution is designed to support:

- Batch-level processing
- Retry mechanisms
- Failed-batch identification
- Processing logs
- Separate raw and processed data

## Azure Architecture

Raw files are stored in Azure Blob Storage and processed before
being loaded into Azure SQL Database.

## Business Value

The solution provides a reliable and scalable pattern for
processing large transactional files and making curated data
available for downstream analytics.

## Portfolio Note

This project uses synthetic data and is an independent portfolio
implementation inspired by real-world data engineering patterns.
It does not contain proprietary code or data from any employer.
