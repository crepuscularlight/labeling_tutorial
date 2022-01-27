#!/usr/bin/env python
# coding=utf-8
# pip install segments-ai
from segments import SegmentsClient, SegmentsDataset
from segments.utils import export_dataset

# Initialize a SegmentsDataset from the release file
client = SegmentsClient('18d8c7ec67a830bae8049ab0e1a2abe127d810da')
release = client.get_release('liudiyang/ARC_MMDETECTION', 'v1') # Alternatively: release = 'flowers-v1.0.json'
dataset = SegmentsDataset(release, labelset='ground-truth', filter_by=['labeled', 'reviewed'])

# Export to COCO panoptic format
export_dataset(dataset, export_format='coco-instance')
