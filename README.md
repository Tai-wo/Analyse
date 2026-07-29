# Analyse — AI Analytics Platform

An AI-powered analytics platform designed to bring the capabilities of **Microsoft Excel, Python, SQL, Tableau, and AI-powered analytics assistance** into a single intelligent workspace.

Analyse is being developed to help users upload datasets, clean and transform data, perform advanced analysis, generate visualizations, build pivot tables, and eventually interact with their data through AI-powered analytical guidance.

The long-term goal is to develop Analyse into a production-quality analytics platform that can support individual analysts, businesses, and organizations with accessible, intelligent, and automated data analysis.

> **Project Status:** Active Development  
> The backend analytics infrastructure is being built incrementally. Several core Excel Engine capabilities have been implemented, while the Chart Engine, additional Excel features, AI-powered recommendations, and frontend-backend integration are still under development.

---

## Project Vision

Traditional analytics workflows often require users to move between multiple tools.

A typical workflow may involve:

```text
Excel
   ↓
Data Cleaning
   ↓
Python / Pandas
   ↓
SQL Analysis
   ↓
Tableau
   ↓
Business Insights

                    ┌─────────────────────┐
                    │       Analyse       │
                    │ AI Analytics        │
                    │ Platform            │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
   Excel Engine           Python Analytics       SQL Analysis
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               │
                               ▼
                      Visualization Engine
                               │
                               ▼
                     AI Analytics Assistant
                               │
                               ▼
                       Business Insights

                       Core Capabilities

Analyse is being developed around several major analytical capabilities.

Data Upload and Management

The platform is designed to allow users to upload datasets and manage them within the analytics workspace.

Supported workflows include:

Dataset upload
Dataset storage
Dataset profiling
Dataset management
Data analysis workflows
Workspace-based analytics
Data Profiling

The profiling system is designed to inspect uploaded datasets and provide information about the structure and quality of the data.

The profiling workflow supports analysis of areas such as:

Dataset dimensions
Column information
Data types
Missing values
Duplicate records
Numerical characteristics
Categorical characteristics
Data quality information

The profiling layer provides the foundation for downstream cleaning, analysis, visualization, and AI-powered recommendations.

Data Cleaning

The cleaning system is being developed to help users prepare datasets for analysis.

The platform is designed to support common data-cleaning operations such as:

Handling missing values
Removing duplicate records
Data type handling
Column transformations
Data preparation
Cleaning workflows

The system is also designed to generate Python-based cleaning code using Pandas, allowing users to understand and reproduce the transformations applied to their datasets.

 Excel Engine

The Excel Engine is a dedicated backend analytics layer designed to reproduce and extend important spreadsheet-based analytical workflows.

The goal is to provide users with familiar Excel-style functionality while building a foundation for more advanced automation and AI-powered analytics.

The Excel Engine is currently under active development.

## Current Excel Engine Structure

backend/
│
├── excel/
│   │
│   ├── features/
│   │   ├── formulas.py
│   │   ├── lookup.py
│   │   ├── pivot.py
│   │   ├── cleaning.py
│   │   ├── filtering.py
│   │   ├── sorting.py
│   │   ├── statistics.py
│   │   └── forecasting.py
│   │
│   └── charts/
│       ├── chart_engine.py
│       ├── chart_recommender.py
│       ├── chart_export.py
│       ├── chart_styles.py
│       ├── chart_utils.py
│       ├── routes.py
│       └── schemas.py

Excel Formula Engine

The Formula Engine provides a foundation for spreadsheet-style calculations within Analyse.

It is designed to allow analytical operations to be performed programmatically while maintaining an Excel-like workflow.

The Formula Engine is one of the completed components of the Excel Engine.

Excel Lookup Engine

The Lookup Engine provides functionality for retrieving and matching data across datasets and columns.

This component is designed to support spreadsheet-style lookup workflows and provide a foundation for more advanced data matching and transformation operations.

The Lookup Engine has been implemented as part of the Excel Engine.

Excel Pivot Engine

The Pivot Engine is one of the most advanced components currently implemented within the Excel Engine.

It is designed to support analytical aggregation and structured data exploration similar to spreadsheet pivot tables.

Current capabilities include:

Basic pivot tables
Crosstabs
Multi-index pivots
Drill-down analysis
Drill-up analysis
Date grouping
Advanced aggregations
Calculated fields
Profit margin analysis
Running totals
Rankings
Contribution analysis
Z-score analysis
Weighted averages
CSV export
Excel export
Workbook export
Styling
Report generation

The Pivot Engine provides a foundation for turning raw datasets into structured analytical summaries.

Excel Chart Engine

The Chart Engine is currently under active development.

Its purpose is to provide Excel-style chart generation within the Analyse backend.

The current implementation is being designed around reusable chart-generation methods that validate input data, generate visualizations, save chart outputs, and record chart-generation activity.

The Chart Engine currently includes implementations for chart types such as:

Bar charts
Horizontal bar charts
Line charts
Area charts
Pie charts
Doughnut charts
Scatter charts
Histograms
Box plots

The architecture also includes supporting components for:

Chart styling
Chart utilities
Chart exporting
Chart generation
Chart reporting

The Chart Engine is not yet considered complete. Additional development is required to improve its production readiness and fully integrate it with the rest of the platform.


AI-Powered Analytics Direction

One of the long-term objectives of Analyse is to move beyond being a traditional analytics application.

The platform is being designed to eventually provide intelligent assistance throughout the analytical workflow.

The intended experience is:

Upload Dataset
      ↓
Profile Dataset
      ↓
Clean Data
      ↓
Analyze Dataset
      ↓
Recommend Analysis
      ↓
Recommend Visualizations
      ↓
Generate Charts
      ↓
Explain Findings
      ↓
Generate Business Insights

Frontend

The frontend is built using:

React
Vite
React Router
CSS
Lucide Icons

The frontend currently contains the following pages and application components:

Login Page
Dashboard
Sidebar
Topbar
Features Page
Upload Page
Results Page
Dataset Page
Workspace Page
History Page
Settings Page

Application routing has been implemented and is currently working correctly.

The Dashboard uses a shared MainLayout structure.

Backend

The backend is built using:

FastAPI
Python
Pandas
OpenPyXL
Plotly
Matplotlib
Seaborn
SQLite
Pydantic

The backend is organized into modular components.

Current backend structure: 

backend/
│
├── auth/
├── charts/
├── cleaning/
├── code_generator/
├── database/
├── dataset_manager/
├── exports/
├── profiling/
├── storage/
├── upload/
├── workspace/
│
└── excel/
    ├── features/
    └── charts/

    Technology Stack
Technology	Used For
React	Frontend application
Vite	Frontend development and build tooling
React Router	Frontend routing
CSS	User interface styling
Lucide Icons	Interface icons
FastAPI	Backend API
Python	Core backend and analytics logic
Pandas	Data manipulation and analysis
OpenPyXL	Excel file processing
Plotly	Interactive chart generation
Matplotlib	Data visualization
Seaborn	Statistical visualization
SQLite	Current application database
Pydantic	Data validation and schemas
Git	Version control
GitHub	Source code hosting

Project Status

Analyse is currently in active development.

The project has progressed beyond the initial application structure and now includes several functional backend analytics modules and a developing Excel Engine.

The current focus is on completing the Excel analytics layer, expanding visualization capabilities, implementing intelligent chart recommendations, and integrating the completed backend functionality into the React frontend.

The project is being developed with a long-term goal of becoming a production-quality AI-powered analytics platform suitable for real-world users and potential commercial deployment.

Project Architecture

The platform follows a modular architecture separating frontend presentation, backend APIs, analytics engines, data management, and visualization capabilities.

Analyse/
│
├── backend/
│   ├── auth/
│   ├── charts/
│   ├── cleaning/
│   ├── code_generator/
│   ├── database/
│   ├── dataset_manager/
│   ├── exports/
│   ├── profiling/
│   ├── storage/
│   ├── upload/
│   ├── workspace/
│   │
│   └── excel/
│       ├── features/
│       │   ├── formulas.py
│       │   ├── lookup.py
│       │   ├── pivot.py
│       │   ├── cleaning.py
│       │   ├── filtering.py
│       │   ├── sorting.py
│       │   ├── statistics.py
│       │   └── forecasting.py
│       │
│       └── charts/
│           ├── chart_engine.py
│           ├── chart_recommender.py
│           ├── chart_export.py
│           ├── chart_styles.py
│           ├── chart_utils.py
│           ├── routes.py
│           └── schemas.py
│
├── frontend/
│
├── .gitignore
└── README.md

Disclaimer

Analyse is an actively developed project. Some features described in this README are currently implemented, while others are under active development or planned for future releases.

The project architecture and feature set may change as development progresses.