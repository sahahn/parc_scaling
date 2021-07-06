---
layout: default
title: Why ensemble boost?
description: Speculation on why ensembles across parcellations provide benefit.
---

# Why does ensembling provide a reliable performance boost?

Ensembling over multiple parcellations shows a [clear advantage over single parcellations](./single_vs_ensemble.html), despite employing random parcellations. So... why?

One obvious potential explanation to the observed ensemble performance gain is that it is due solely to an inherent utility of ensembling, which has been shown to reliably increase performance across a wide range of ML applications ([Dietterich 2000](https://dl.acm.org/doi/10.5555/648054.743935), [Zhou 2009](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/springerEBR09.pdf)). This is likely true in our case, noting the outsized performance of the 'All' ensemble relative to the SVM based ensemble as
seen on page [Whats Best](./whats_best.html).

On the other hand, ensembles as employed in this work are specifically designed to capture information from multiple overlapping parcellations. It is plausible that the performance boost obtained by this methodology may be related to the boost from increasing resolution; this could indicate that the “true” best parcellations are not neat and uniform. Instead, by allowing overlapping parcellations, more predictive information can be extracted despite noisy ground truth data. Alternatively, it could also be that ensembling over multiple views provides benefit by forcing different classifiers to exploit different unique predictive signals ([Allen-Zhu 2020](https://arxiv.org/abs/2012.09816)). The cortical surface exhibits high covariance between different brain regions on measures employed as inputs features (e.g., cortical thickness); it may therefore be reasonable to assume that there are more than one multivariate predictive patterns capable of performing well out of sample on the target of interest ([Alexander-Bloch 2013](https://www.jneurosci.org/content/33/7/2889)). In this case, different instances of random parcellations may help base estimators of the ensemble learn distinct predictive patterns that when combined can exploit a larger region of competency when generating predictions for new samples.

## References

- [Alexander-Bloch, A., Raznahan, A., Bullmore, E., & Giedd, J. (2013). The convergence of maturational change and structural covariance in human cortical networks. Journal of Neuroscience, 33(7), 2889-2899.](https://www.jneurosci.org/content/33/7/2889)

- [Allen-Zhu, Z., & Li, Y. (2020). Towards Understanding Ensemble, Knowledge Distillation and Self-Distillation in Deep Learning. arXiv preprint arXiv:2012.09816.](https://arxiv.org/abs/2012.09816)

- [Dietterich, T. G. (2000, June). Ensemble methods in machine learning. In International workshop on multiple classifier systems (pp. 1-15). Springer, Berlin, Heidelberg.](https://dl.acm.org/doi/10.5555/648054.743935)

- [Zhou, Z. H. (2009). Ensemble learning. Encyclopedia of biometrics, 1, 270-273.](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/springerEBR09.pdf)