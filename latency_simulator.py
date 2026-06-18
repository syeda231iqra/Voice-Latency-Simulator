import time


def run_pipeline(name, steps):
    print(f"\n{name}")
    print("-" * len(name))
    total = 0

    for step_name, duration in steps:
        print(f"{step_name} started...")
        time.sleep(0.3)  # Short demo delay instead of real full duration
        print(f"{step_name} completed in {duration} ms")
        total += duration

    print(f"Total estimated latency: {total} ms")
    return total


traditional_pipeline = [
    ("Wait for full user audio", 3000),
    ("Speech-to-Text processing", 1200),
    ("LLM response generation", 1800),
    ("Text-to-Speech generation", 1400),
    ("Audio playback start", 300),
]

streaming_pipeline = [
    ("Streaming audio chunks while user speaks", 500),
    ("Streaming STT partial transcript", 600),
    ("Early LLM response generation", 1200),
    ("Streaming TTS first audio chunk", 700),
    ("Audio playback start", 200),
]


if __name__ == "__main__":
    traditional = run_pipeline("Traditional Voice AI Pipeline", traditional_pipeline)
    streaming = run_pipeline("Optimized Streaming Voice AI Pipeline", streaming_pipeline)

    improvement = traditional - streaming

    print("\nSummary")
    print("-------")
    print(f"Traditional latency: {traditional} ms")
    print(f"Streaming latency: {streaming} ms")
    print(f"Estimated improvement: {improvement} ms")

    print("\nKey idea:")
    print("Streaming reduces latency because the system starts processing audio before the user finishes speaking.")
