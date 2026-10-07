# Schnelle Matrixberechnung für künstliche Intelligenz

DeepGEMM, entwickelt von DeepSeek, ist eine Open-Source-Bibliothek für grundlegende lineare Algebra-Unterprogramme (BLAS), die Matrixmultiplikationsoperationen auf Grafikprozessoren (GPUs) beschleunigt. Die Software bietet optimierte Kernel (Kernels) für KI-Modelle, die Hochleistungsrechnen erfordern.

- ★ 8.528
- Cuda
- GitHub Trending · 2026-10-06

## Was es bringt
- Verkürzt die Laufzeiten großer Sprachmodelle durch Beschleunigung von Matrixmultiplikationen.
- Kompiliert Kernel automatisch zur Laufzeit, ohne während der Installation auf die CUDA-Kompilierung warten zu müssen.
- Reduziert Kommunikationsverluste der Grafikkarte, indem verschiedene Expertenmodelle in einer einzigen Operation kombiniert werden.

## Installation
**Klonen des Repositories und Entwicklungsumgebung h**

```
# Submodule must be cloned
git clone --recursive git@github.com:deepseek-ai/DeepGEMM.git
cd DeepGEMM

# Link some essential includes and build the C++ extension
cat develop.sh
./develop.sh
```

**Bibliothek installieren**

```
cat install.sh
./install.sh
```


## Wenn Sie nicht programmieren
Ich möchte die DeepGEMM-Bibliothek auf meiner Hardware mit NVIDIA SM90- oder SM100-Architektur installieren. Führen Sie zuerst die Befehle '# Submodule must be cloned\ngit clone --recursive git@github.com:deepseek-ai/DeepGEMM.git\ncd DeepGEMM\n\n# Link some essential includes and build the C++ extension\ncat develop.sh\n./develop.sh' aus, um das Repository mit seinen Submodulen zu klonen und die Entwicklungsumgebung vorzubereiten. Führen Sie anschließend den Befehl 'cat install.sh\n./install.sh' aus, um die Installation abzuschließen, und machen Sie die Bibliothek in der Python-Umgebung mit dem Befehl 'import deep_gemm' einsatzbereit.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/deepgemm/
