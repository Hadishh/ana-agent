# Use NVIDIA’s CUDA runtime as base (adjust CUDA version if you need)
FROM vllm/vllm-openai:v0.7.2


# Set a working directory
WORKDIR /workspace

# Copy your two launcher scripts in
COPY vllm_serve.sh vllm_embedding.sh /workspace/
COPY .env /workspace/
# Make sure they’re executable
RUN chmod +x /workspace/vllm_serve.sh /workspace/vllm_embedding.sh

# Default to bash for interactive use
CMD ["bash"]
