# Deepseek-R1-qwen1.5B
how to run DeepSeek-R1-Distill-Qwen-1.5B GGUF locally on your PC


### technology stack
Run the model with llama.cpp binaries, Vulkan flavour

- Download the ZIP archive llama-b4539-bin-win-vulkan-x64.zip from [the official Repo](https://github.com/ggerganov/llama.cpp/releases/download/b4539/llama-b4539-bin-win-vulkan-x64.zip)
- extract the ZIP archive directly in the project directory
- download the GGUF from the [Bartowski repo](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF) I used the [DeepSeek-R1-Distill-Qwen-1.5B-Q6_K.gguf](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q6_K.gguf?download=true)
- open the terminal and run `start cmd.exe /k "llama-server.exe -m DeepSeek-R1-Distill-Qwen-1.5B-Q6_K.gguf -c 15000 -ngl 999"`

As for the python environemnt you need:
- my prommpt library `promptLibv2Qwen.py` from this folder
- `pip install openai`
- the python file `runDeepSeekR1.py` from this folder 

From the terminal with the `venv` activated run
```
python runDeepSeekR1.py
```




For months I have done the wrong things. But llama.cpp now has pre-compiled binaries at every release. So, for instance, starting from revision b4351 llama.cpp supports also the Falcon3 models.

To be inclusive (all kind of hardware) we will use the binaries for AXV2 support, from release b4358 (the one available at the time of this newsletter writing).

Download the file in your project directory: for me is Falcon3. Create a sub-folder called llamacpp and inside another one called model (we will download the GGF for Falcon3 there).

<img src='https://github.com/fabiomatricardi/Falcon3-1B-it-llamaCPP/raw/main/image001.png' width=800>

Unzip all files in the [llama-b4539-bin-win-vulkan-x64.zip](https://github.com/ggerganov/llama.cpp/releases/download/b4539/llama-b4539-bin-win-vulkan-x64.zip)  archive into the llamacpp directory

<img src='https://github.com/fabiomatricardi/Falcon3-1B-it-llamaCPP/raw/main/image002.png' width=800>

- download the GGUF from the [Bartowski repo](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF) I used the [DeepSeek-R1-Distill-Qwen-1.5B-Q6_K.gguf](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q6_K.gguf?download=true). Save the GGUF file in the subdirectory llamacpp\model.

<img src='https://github.com/fabiomatricardi/Falcon3-1B-it-llamaCPP/raw/main/image003.png' width=800>

Open a terminal window in the subdirectory llamacpp, and run
```
start cmd.exe /k "llama-server.exe -m model/DeepSeek-R1-Distill-Qwen-1.5B-Q6_K.gguf -c 15000 -ngl 999"
```

In another terminal with the venv activated run
```
python runDeepSeekR1.py
```
