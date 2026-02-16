# Knowledge Graph — High-Level View

```mermaid
flowchart TB
    subgraph documents["Document nodes (2)"]
        D1["Doc 1: Mental Health Guide<br/>+ summary, headlines, embedding"]
        D2["Doc 2: Health & Wellness Guide<br/>+ summary, headlines, embedding"]
    end

    subgraph chunks1["Chunks from Doc 1"]
        C1_1["Chunk 1.1<br/>entities, themes"]
        C1_2["Chunk 1.2<br/>entities, themes"]
        C1_3["Chunk 1.3<br/>entities, themes"]
    end

    subgraph chunks2["Chunks from Doc 2"]
        C2_1["Chunk 2.1<br/>entities, themes"]
        C2_2["Chunk 2.2<br/>entities, themes"]
        C2_3["Chunk 2.3<br/>entities, themes"]
    end

    D1 -->|child| C1_1
    D1 -->|child| C1_2
    D1 -->|child| C1_3
    D2 -->|child| C2_1
    D2 -->|child| C2_2
    D2 -->|child| C2_3

    C1_1 -.->|next| C1_2
    C1_2 -.->|next| C1_3
    C2_1 -.->|next| C2_2
    C2_2 -.->|next| C2_3

    C1_2 <-->|cosine_similarity| C2_1
    C1_1 <-->|entities_overlap| C2_2
```

**Legend**
- **Document nodes**: Full `page_content` plus `headlines`, `summary`, `summary_embedding`.
- **Chunk nodes**: Section-level `page_content` plus `entities` and `themes`.
- **child**: Document → chunk (ownership).
- **next**: Chunk → chunk (order within a document).
- **cosine_similarity** / **entities_overlap**: Chunk ↔ chunk (similarity/overlap; can be across documents).

You can paste the Mermaid block into [Mermaid Live](https://mermaid.live) or any Markdown viewer that supports Mermaid to render the diagram.
