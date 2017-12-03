{
  "targets": [
    {
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "target_name": "mycppaddon",
      "sources": [ "cppaddon.cpp" ]
    }
  ]
}