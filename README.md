# Voice AI Latency Simulator

A simple Python project that explains latency in Voice AI systems.

## What this project shows
Voice AI systems can feel slow if each step waits for the previous step to fully finish.

This project compares:

1. Traditional pipeline
2. Optimized streaming pipeline

## Traditional Flow

**Full Audio → STT → LLM → TTS → Playback**

## Streaming Flow

**Audio Chunks → Streaming STT → Early LLM → Streaming TTS → Playback**

## Run

```bash
python latency_simulator.py
```

## Why this matters
For real-time voice agents, latency is one of the most important user-experience problems. Users expect the assistant to respond naturally, without long pauses.

## Ways to Reduce Latency
- Use streaming STT
- Use streaming TTS
- Use WebSockets
- Use faster LLM models
- Keep prompts short
- Cache repeated answers
- Reduce unnecessary RAG calls
- Monitor every pipeline stage separately

## Explanation
I built this simulator to show that I understand latency in voice AI. A production system should not wait for the complete audio file if streaming is possible. It should process small audio chunks, generate partial transcripts, and start the response earlier.
