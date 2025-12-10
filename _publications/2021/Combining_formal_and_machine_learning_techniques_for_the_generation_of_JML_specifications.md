---
title: "Combining formal and machine learning techniques for the generation of JML specifications"
authors:
  - Armand Puccetti
  - Gaël Chalendar
  - Pierre-Yves Gibello
date: 2021-01-01
venue: "Proceedings of the 23rd {ACM} {International} {Workshop} on {Formal} {Techniques} for {Java}-like {Programs}"
venue_short: "Proceedings 23rd"
type: conference
links:
  paper: https://doi.org/10.1145/3464971.3468425
---

Producing maintainable programs is a big challenge for the software industry as it requires solid Engineering skills and efficient CASE tools. Often, industrial programs are of a very large size (more than 1M SLOC), use high-level programming languages to their full extent (e.g. C++20, Ada 2005 or Java 16), are provided with scarce and often outdated documentation partially written in natural language. Maintenance engineers are therefore in need to understand the application at hand starting from the material left behind by the developers. The European H2020 Project DECODER (https://www.decoder- project.eu) addresses this problem by proposing to combine Natural Language Processing techniques and Formal Methods to turn as best as possible code artifacts into formal data allowing to reduce the maintenance costs and thus the total costs of ownership. In this context, we will show how to generate JML annotations using a combination of 1) automatic generation of minimal predicates, 2) Natural Language Processing (NLP) based predicates generator, and 3) manual refinement and correction, to instrument and enhance code and documentation. We will illustrate it on code samples from the MyThaiStar (https://github.com/devonfw/my- thai-star) application developed with the CASE tool devonfw by CAP GEMINI, and the Joram JMS implementation (https://gitlab.ow2.org/joram/joram) from OW2 code base.
