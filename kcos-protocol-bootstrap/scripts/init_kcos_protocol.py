from __future__ import annotations

import argparse
from pathlib import Path


def get_skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_protocol_template(filename: str) -> str:
    template_path = get_skill_root() / "assets" / "protocol" / filename
    return template_path.read_text(encoding="utf-8")


def load_script_template(filename: str) -> str:
    template_path = get_skill_root() / "assets" / "scripts" / filename
    return template_path.read_text(encoding="utf-8")


def write_text(path: Path, content: str, force: bool) -> str:
    existed_before = path.exists()
    if existed_before and not force:
        return "skipped"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "updated" if existed_before else "created"


def ensure_directory(path: Path) -> str:
    if path.exists():
        return "skipped"
    path.mkdir(parents=True, exist_ok=True)
    return "created"


def build_root_knowledge_readme() -> str:
    return """# 知识库总览

## 目录用途

本目录存放项目的结构化知识资产，包括业务逻辑、架构设计、决策记录和可复用模式。

## 一级目录

- `business-logic/`：业务流程、隐性规则、执行链路
- `architecture/`：系统架构、方案设计、演进路线
- `requirements/`：需求分析、范围边界、验收标准
- `decisions/`：关键决策记录（ADR）
- `patterns/`：可复用工程模式与模板
- `rpa/`：RPA 案例与资产规范

## 维护约束

- 参考 `KCOS/protocol/p0-rules.md`
- 知识文档改动后执行 `python3 KCOS/scripts/kcos_p0.py sync`
"""


def build_subdir_readme(title: str, purpose: str) -> str:
    return f"""# {title}

## 目录说明

{purpose}

## 维护约束

- 文档建议带 `KCOS-Index` front matter。
- 仅使用相对路径链接项目内文档。
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize KCOS protocol baseline")
    parser.add_argument("--root", default=".", help="Target repository root")
    parser.add_argument("--force", action="store_true", help="Overwrite existing baseline files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    kcos_root = root / "KCOS"
    protocol_root = kcos_root / "protocol"

    directory_targets = [
        kcos_root / "context",
        kcos_root / "knowledge",
        kcos_root / "templates",
        kcos_root / "assets",
        kcos_root / "scripts",
        kcos_root / ".kcos",
        protocol_root,
    ]

    knowledge_targets = {
        "business-logic": "沉淀业务流程、隐性规则和执行链路。",
        "architecture": "沉淀架构设计、模块边界和演进方案。",
        "requirements": "沉淀需求分析、范围边界与验收标准。",
        "decisions": "沉淀关键决策记录（ADR）。",
        "patterns": "沉淀可复用工程模式和模板。",
        "rpa": "沉淀 RPA 案例资产与脚本规范。",
    }

    directory_results: list[tuple[Path, str]] = []
    file_results: list[tuple[Path, str]] = []

    for directory_path in directory_targets:
        result = ensure_directory(directory_path)
        directory_results.append((directory_path, result))

    protocol_files = {
        "p0-rules.md": load_protocol_template("p0-rules.md"),
        "ai-playbook.md": load_protocol_template("ai-playbook.md"),
        "README.md": load_protocol_template("README.md"),
    }

    for filename, content in protocol_files.items():
        target_path = protocol_root / filename
        result = write_text(target_path, content, args.force)
        file_results.append((target_path, result))

    script_files = {
        "kcos_p0.py": load_script_template("kcos_p0.py"),
    }

    for filename, content in script_files.items():
        target_path = kcos_root / "scripts" / filename
        result = write_text(target_path, content, args.force)
        file_results.append((target_path, result))

    knowledge_root_readme_path = kcos_root / "knowledge" / "README.md"
    root_readme_result = write_text(knowledge_root_readme_path, build_root_knowledge_readme(), args.force)
    file_results.append((knowledge_root_readme_path, root_readme_result))

    for subdir, purpose in knowledge_targets.items():
        subdir_path = kcos_root / "knowledge" / subdir
        subdir_result = ensure_directory(subdir_path)
        directory_results.append((subdir_path, subdir_result))
        subdir_readme_path = subdir_path / "README.md"
        readme_result = write_text(subdir_readme_path, build_subdir_readme(subdir, purpose), args.force)
        file_results.append((subdir_readme_path, readme_result))

    print(f"[KCOS] target root: {root}")
    print("[KCOS] directories:")
    for path, status in directory_results:
        print(f"- {status:7} {path.relative_to(root)}")

    print("[KCOS] files:")
    for path, status in file_results:
        print(f"- {status:7} {path.relative_to(root)}")

    sync_script = kcos_root / "scripts" / "kcos_p0.py"
    if sync_script.exists():
        print("[KCOS] next: python3 KCOS/scripts/kcos_p0.py sync")
    else:
        print("[KCOS] notice: KCOS/scripts/kcos_p0.py not found, skip sync for now")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
