"""Current version of Scalene; reported by --version."""

scalene_version = "1.5.37"
scalene_date = "2024.03.10"

# Port to use for Scalene UI
SCALENE_PORT = 11235

# Must equal src/include/sampleheap.hpp NEWLINE *minus 1*
NEWLINE_TRIGGER_LENGTH = 98820  # SampleHeap<...>::NEWLINE-1
