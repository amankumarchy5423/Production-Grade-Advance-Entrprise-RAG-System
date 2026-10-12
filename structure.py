
from pathlib import Path

PROJECT_NAME = "Production-Grade-Advance-Entrprise-RAG-System"

DIRECTORIES = [
    "src/aman-enterprise_rag/api/routes",
    "src/aman-enterprise_rag/ingestion/loaders",
    "src/aman-enterprise_rag/ingestion/chunking",
    "src/aman-enterprise_rag/retrieval",
    "src/aman-enterprise_rag/generation",
    "src/aman-enterprise_rag/agents/nodes",
    "src/aman-enterprise_rag/rag",
    "src/aman-enterprise_rag/gateway",
    "src/aman-enterprise_rag/guardrails",
    "src/aman-enterprise_rag/evaluation",
    "src/aman-enterprise_rag/observability",
    "src/aman-enterprise_rag/schemas",
    "ui/components",
    "evals/datasets",
    "tests/unit",
    "tests/integration",
    "scripts",
    "configs",
    "data/raw",
    "data/processed",
    "docs",
    "deployment/docker",
    "deployment/aws",
    ".github/workflows",
]

FILES = [
    # Application entrypoint and configuration
    "src/enterprise_rag/__init__.py",
    "src/enterprise_rag/main.py",
    "src/enterprise_rag/config.py",

    # API
    "src/enterprise_rag/api/__init__.py",
    "src/enterprise_rag/api/dependencies.py",
    "src/enterprise_rag/api/middleware.py",
    "src/enterprise_rag/api/routes/__init__.py",
    "src/enterprise_rag/api/routes/health.py",
    "src/enterprise_rag/api/routes/query.py",
    "src/enterprise_rag/api/routes/documents.py",

    # Ingestion
    "src/enterprise_rag/ingestion/__init__.py",
    "src/enterprise_rag/ingestion/loaders/__init__.py",
    "src/enterprise_rag/ingestion/loaders/pdf.py",
    "src/enterprise_rag/ingestion/loaders/html.py",
    "src/enterprise_rag/ingestion/loaders/text.py",
    "src/enterprise_rag/ingestion/loaders/docx.py",
    "src/enterprise_rag/ingestion/loaders/pptx.py",
    "src/enterprise_rag/ingestion/chunking/__init__.py",
    "src/enterprise_rag/ingestion/chunking/splitter.py",
    "src/enterprise_rag/ingestion/embeddings.py",
    "src/enterprise_rag/ingestion/pipeline.py",

    # Retrieval
    "src/enterprise_rag/retrieval/__init__.py",
    "src/enterprise_rag/retrieval/vector_store.py",
    "src/enterprise_rag/retrieval/retriever.py",
    "src/enterprise_rag/retrieval/hybrid_search.py",
    "src/enterprise_rag/retrieval/reranker.py",
    "src/enterprise_rag/retrieval/filters.py",

    # Generation
    "src/enterprise_rag/generation/__init__.py",
    "src/enterprise_rag/generation/prompts.py",
    "src/enterprise_rag/generation/llm.py",
    "src/enterprise_rag/generation/citations.py",

    # LangGraph agents
    "src/enterprise_rag/agents/__init__.py",
    "src/enterprise_rag/agents/state.py",
    "src/enterprise_rag/agents/graph.py",
    "src/enterprise_rag/agents/nodes/__init__.py",
    "src/enterprise_rag/agents/nodes/planner.py",
    "src/enterprise_rag/agents/nodes/retriever.py",
    "src/enterprise_rag/agents/nodes/responder.py",
    "src/enterprise_rag/agents/nodes/grader.py",

    # RAG orchestration
    "src/enterprise_rag/rag/__init__.py",
    "src/enterprise_rag/rag/chain.py",
    "src/enterprise_rag/rag/pipeline.py",

    # LLM gateway and guardrails
    "src/enterprise_rag/gateway/__init__.py",
    "src/enterprise_rag/gateway/llm_gateway.py",
    "src/enterprise_rag/guardrails/__init__.py",
    "src/enterprise_rag/guardrails/input_guard.py",
    "src/enterprise_rag/guardrails/output_guard.py",

    # Evaluation and observability
    "src/enterprise_rag/evaluation/__init__.py",
    "src/enterprise_rag/evaluation/evaluator.py",
    "src/enterprise_rag/evaluation/datasets.py",
    "src/enterprise_rag/evaluation/metrics.py",
    "src/enterprise_rag/observability/__init__.py",
    "src/enterprise_rag/observability/tracing.py",
    "src/enterprise_rag/observability/logging.py",
    "src/enterprise_rag/observability/metrics.py",

    # Request and response schemas
    "src/enterprise_rag/schemas/__init__.py",
    "src/enterprise_rag/schemas/query.py",
    "src/enterprise_rag/schemas/documents.py",

    # UI
    "ui/app.py",
    "ui/components/chat.py",

    # Evaluation suites
    "evals/run_evaluation.py",
    "evals/test_rag_quality.py",
    "evals/datasets/README.md",

    # Automated tests
    "tests/conftest.py",
    "tests/unit/test_chunking.py",
    "tests/unit/test_retrieval.py",
    "tests/unit/test_guardrails.py",
    "tests/integration/test_ingestion_pipeline.py",
    "tests/integration/test_query_api.py",

    # Utility scripts
    "scripts/ingest.py",
    "scripts/evaluate.py",
    "scripts/build_index.py",

    # Configuration and data
    "configs/config.yaml",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/README.md",

    # Documentation
    "docs/architecture.md",
    "docs/setup.md",
    "docs/deployment.md",
    "docs/evaluation.md",
    "docs/operations.md",

    # Deployment
    "deployment/docker/Dockerfile",
    "deployment/aws/README.md",

    # CI/CD
    ".github/workflows/ci.yml",
    ".github/workflows/cd.yml",

    # Root files
    ".env.example",
    ".gitignore",
    "docker-compose.yml",
    "Makefile",
    "pyproject.toml",
    "requirements.txt",
    "requirements-dev.txt",
    "README.md",
]


def create_project_structure():
    # root = Path(PROJECT_NAME)
    # root.mkdir(parents=True, exist_ok=True)

    created_dirs = 0
    created_files = 0
    existing_files = 0

    for directory in DIRECTORIES:
        path = Path(directory)

        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created_dirs += 1

    package_dirs = [
         "src" / "enterprise_rag",
        *[
            directory
            for directory in DIRECTORIES
            if directory.startswith("src/enterprise_rag/")
        ],
    ]

    for directory in package_dirs:
        if directory.is_dir():
            init_file = directory / "__init__.py"

            if not init_file.exists():
                init_file.touch()
                created_files += 1

    # for filename in FILES:
    #     path = root / filename
    #     path.parent.mkdir(parents=True, exist_ok=True)

    #     if path.exists():
    #         existing_files += 1
    #         continue

    #     path.touch()
    #     created_files += 1

    # print(f"\nProject created at: {root.resolve()}")
    print(f"Directories created: {created_dirs}")
    print(f"Files created:      {created_files}")
    print(f"Files preserved:    {existing_files}")
    print("\nNote: files are empty scaffolds, not implementations.")


if __name__ == "__main__":
    create_project_structure()
