---
title: "GeSERA: General-domain Summary Evaluation by Relevance Analysis"
authors:
  - Jessica López Espejel
  - Gaël Chalendar
  - Jorge Garcia Flores
  - Thierry Charnois
  - Ivan Vladimir Meza Ruiz
date: 2021-01-01
venue: "Proceedings of the {International} {Conference} on {Recent} {Advances} in {Natural} {Language} {Processing} ({RANLP} 2021)"
venue_short: "Proceedings {International}"
type: conference
selected: false
links:
  paper: https://aclanthology.org/2021.ranlp-main.98
---

We present GeSERA, an open-source improved version of SERA for evaluating automatic extractive and abstractive summaries from the general domain. SERA is based on a search engine that compares candidate and reference summaries (called queries) against an information retrieval document base (called index). SERA was originally designed for the biomedical domain only, where it showed a better correlation with manual methods than the widely used lexical-based ROUGE method. In this paper, we take out SERA from the biomedical domain to the general one by adapting its content-based method to successfully evaluate summaries from the general domain. First, we improve the query reformulation strategy with POS Tags analysis of general-domain corpora. Second, we replace the biomedical index used in SERA with two article collections from AQUAINT-2 and Wikipedia. We conduct experiments with TAC2008, TAC2009, and CNNDM datasets. Results show that, in most cases, GeSERA achieves higher correlations with manual evaluation methods than SERA, while it reduces its gap with ROUGE for general-domain summary evaluation. GeSERA even surpasses ROUGE in two cases of TAC2009. Finally, we conduct extensive experiments and provide a comprehensive study of the impact of human annotators and the index size on summary evaluation with SERA and GeSERA.
