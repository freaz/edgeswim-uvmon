{
  "targets": [
    {
      "include_dirs" : [
          "<!(node -e \"require('nan')\")"
      ],
      "target_name": "uvmon",
      "sources": ["uvmon.cc", "histogram.cc", "profiler_wrapper.cc"]
    }
  ]
}
