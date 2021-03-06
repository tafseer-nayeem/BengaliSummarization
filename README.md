## Bengali Summarization (BenSumm)

Code and Dataset of our work, [Unsupervised Abstractive Summarization of Bengali Text Documents](https://www.aclweb.org/anthology/2021.eacl-main.224/) accepted at [EACL 2021](https://2021.eacl.org/). 

- [Dataset](https://github.com/tafseer-nayeem/BengaliSummarization/tree/main/Dataset)
	- [BNLPC](https://github.com/tafseer-nayeem/BengaliSummarization/tree/main/Dataset/BNLPC)
	- [NCTB](https://github.com/tafseer-nayeem/BengaliSummarization/tree/main/Dataset/NCTB)
- [Presentation](https://tafseer-nayeem.github.io/files/EACL2021/eacl2021_presentation.pdf)
- [Poster](https://tafseer-nayeem.github.io/files/EACL2021/eacl2021_poster.pdf)
- [Demo Video](https://youtu.be/LrnskktiXcg)

## Instructions

Download the pretrained ULMFiT model named `export.pkl` from this [link](https://drive.google.com/drive/folders/11ynzy-mX2zF4JsYruwDftMvXGCY2dTzi?usp=sharing) and place it in the `Code/AbstractiveSummarizer/model/` directory. 

**Note:** If you find some errors, you may try downgrading PyTorch, FastAI, and NetworkX. 

## Authors

- Radia Rayan Chowdhury*
- Mir Tafseer Nayeem*
- Tahsin Tasnim Mim
- Md. Saifur Rahman Chowdhury
- Taufiqul Jannat

*[Equal Contribution]

## Citation

If you use any of the resources or it's relevant to your work, please cite the paper. 

```
@inproceedings{chowdhury2021eacl,
    title = "Unsupervised Abstractive Summarization of Bengali Text Documents",
    author  = {Radia Rayan Chowdhury and Mir Tafseer Nayeem and Tahsin Tasnim Mim and Md. Saifur Rahman Chowdhury and Taufiqul Jannat},
    booktitle = "Proceedings of the 16th Conference of the {E}uropean Chapter of the Association for Computational Linguistics (EACL)",
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics"
}
```