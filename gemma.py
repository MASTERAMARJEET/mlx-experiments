import subprocess

from dotenv import load_dotenv
from mlx_vlm import load, stream_generate
from mlx_vlm.prompt_utils import apply_chat_template
from mlx_vlm.utils import load_config

load_dotenv()


def stream_text(hf_repo, prompt):
    model, processor = load(hf_repo)
    config = load_config(hf_repo)

    formatted_prompt = apply_chat_template(processor, config, prompt)
    for result in stream_generate(model, processor, formatted_prompt, verbose=False):
        yield result.text
    yield result.prompt_tps


def serve(hf_repo):
    subprocess.run(["mlx_vlm.server", "--port", "8080", "--model", hf_repo])


if __name__ == "__main__":
    serve("mlx-community/gemma-4-e2b-it-5bit")
