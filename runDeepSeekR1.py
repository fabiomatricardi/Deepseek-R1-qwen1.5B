# Chat with an intelligent assistant in your terminal  with DeepSeek-R1-Distill-Qwen-1.5B-Q6_K.gguf
# model served in another terminal window with llama-server
from openai import OpenAI
import sys
from time import sleep
import warnings
warnings.filterwarnings(action='ignore')

STOPS = ['<´¢£endÔûüofÔûüsentence´¢£>']
COUNTERLIMITS = 10  #an even number
modelname = 'DeepSeek-R1-Distill-Qwen-1.5B'
NCTX = 131072

# ASCII ART FROM https://asciiart.club/
print("\033[94m")
t = """                                                                           
                                                                                

     ,╓╗╗╗╗@╢`  ]╗²   ,                                                         
   ╓╢▒▒▒▒▒▒▒▒║╖  ║▒║╢▒║                                               ,         
  ]▒╙╙╙╝╢▒▒▒▒╢╢▒╗╖╢▒`     ,╓ ║[ ,╓╖╓   ╓╖╖  ╓╖╓╖,  ,╓╖╖   ╓╓╖,  ,╓╖╓  ▒   ╓     
  ]▒      ╙▒▒║[ ╢▒▒║     ╢`  ║[]╜ ╓╓╢ ╢ ╓╓║ ║╜  ╙║ ╢╖╓╓  ╢`╓╓║[]╝ ╓╓╢ ▒ ╖╜      
   ╢╢       ╢▒▒▒▒▒╝      ╙╖²╓╢[ ║╖╓╖r ║╖╓╓m ║[┌╓╢┘ ╗╖,╓╢ ╙╗╓╓╗  ║╖╓╖r ▒  ║╖     
    ╙▒╗, ╙@╖ ╙║▒▒▒                          ║[                                  
      ╙╝║▒▒▒╢╝╜²`"`                                                             
                                                                      

                              ║║╢╢╢╢╢╢╢@╗ ,,╓╗╢╢╢[                              
                              ▒▒▒▒```║▒▒▒╢▒║╝║▒▒▒                               
                             ║▒▒▒▒║╢╢▒▒╢`    ▒▒▒[                               
                             ▒▒▒▒   ▒▒▒▒    ]▒▒▒                                
                             ````   ````    ````                                

             
"""
print(t)

# Point to the local server
client = OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed", organization=modelname)
print(f"✅ Ready to Chat with {modelname} Context length={NCTX} tokens...")
print("\033[0m")  #reset all

history = [
]
print("\033[92;1m")
counter = 1
while True:
    if counter > COUNTERLIMITS:
        history = [
        ]        
    userinput = ""
    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows) - type quit! to exit the chatroom:")
    print("\033[91;1m")  #red
    lines = sys.stdin.readlines()
    for line in lines:
        userinput += line + "\n"
    if "quit!" in lines[0].lower():
        print("\033[0mBYE BYE!")
        break
    history.append({"role": "user", "content": userinput})
    print("\033[92;1m")

    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=history,
        temperature=0.3,
        frequency_penalty  = 1.6,
        max_tokens = 1000,
        stream=True,
        stop=STOPS
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content
    history.append(new_message)  
    counter += 1  


##############MODEL CARD##########################################
"""
# Chat with an intelligent assistant in your terminal  
# MODEL: DeepSeek R1 Distill Qwen 1.5B
# Original model: from BARTOWSKI REPO
# DeepSeek-R1-Distill-Qwen-1.5B-Q6_K.gguf
MODELCARD
===========================================================
mp = 'DeepSeek-R1-Distill-Qwen-1.5B-Q6_K.gguf'


CHAT TEMPLATE = yes
NCTX = 131072
print_info: arch             = qwen2
print_info: vocab_only       = 0
print_info: n_ctx_train      = 131072
print_info: n_embd           = 1536
print_info: n_layer          = 28
print_info: n_head           = 12
print_info: n_head_kv        = 2
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 6
print_info: n_embd_k_gqa     = 256
print_info: n_embd_v_gqa     = 256
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: n_ff             = 8960
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 131072
print_info: rope_finetuned   = unknown
print_info: ssm_d_conv       = 0
print_info: ssm_d_inner      = 0
print_info: ssm_d_state      = 0
print_info: ssm_dt_rank      = 0
print_info: ssm_dt_b_c_rms   = 0
print_info: model type       = 1.5B
print_info: model params     = 1.78 B
print_info: general.name     = DeepSeek R1 Distill Qwen 1.5B
print_info: vocab type       = BPE
print_info: n_vocab          = 151936
print_info: n_merges         = 151387
print_info: BOS token        = 151646 '<´¢£beginÔûüofÔûüsentence´¢£>'
print_info: EOS token        = 151643 '<´¢£endÔûüofÔûüsentence´¢£>'
print_info: EOT token        = 151643 '<´¢£endÔûüofÔûüsentence´¢£>'
print_info: PAD token        = 151643 '<´¢£endÔûüofÔûüsentence´¢£>'
print_info: LF token         = 148848 '├ä─¼'
print_info: FIM PRE token    = 151659 '<|fim_prefix|>'
print_info: FIM SUF token    = 151661 '<|fim_suffix|>'
print_info: FIM MID token    = 151660 '<|fim_middle|>'
print_info: FIM PAD token    = 151662 '<|fim_pad|>'
print_info: FIM REP token    = 151663 '<|repo_name|>'
print_info: FIM SEP token    = 151664 '<|file_sep|>'
print_info: EOG token        = 151643 '<´¢£endÔûüofÔûüsentence´¢£>'
print_info: EOG token        = 151662 '<|fim_pad|>'
print_info: EOG token        = 151663 '<|repo_name|>'
print_info: EOG token        = 151664 '<|file_sep|>'

"""    