---
title: "Saucissonnage of Long Sequences into a Multi-encoder for Neural Text Summarization with Transformers"
authors:
  - Jessica López Espejel
  - Gaël Chalendar
  - Jorge Garcia Flores
  - Ivan Vladimir Meza Ruiz
  - Thierry Charnois
date: 2021-01-01
venue: "Extraction et Gestion des Connaissances ({EGC}) 2021"
venue_short: "EGC"
type: conference
selected: false
links:
  paper: https://hal.science/hal-04090684
---

Transformer deep models have gained lots of attraction in Neural Text Summarization. The problem with existing Transformer-based systems is that they truncate documents considerably before feeding them to the network. In this paper, we are particularly interested in biomedical long text summarization. However, current input sequences are far shorter than the average length of biomedical articles. To handle this problem, we propose two improvements to the original Transformer model that allow a faster training of long sequences without penalizing the summary quality. First, we split the input between four encoders to focus attention on smaller segments of the input. Second, we use end-chunk task training at the decoder level for progressive fast decoding. We evaluate our proposed architecture on {PubMed}, a well-known biomedical dataset. The comparison with competitive baselines shows that our approach: (1) allows reading large input sequences, (2) reduces the training time considerably, and (3) slightly improves the quality of generated summaries.
