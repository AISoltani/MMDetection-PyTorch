# Copyright (c) OpenMMLab. All rights reserved.
#Import Libraries

from mmengine.config import read_base
from mmengine.model.weight_init import PretrainedInit

with read_base():
    from .detr_r50_8xb2_500e_coco import *

model.update(
    dict(
        backbone=dict(
            depth=18,
            init_cfg=dict(
                type=PretrainedInit, checkpoint='torchvision://resnet18')),
        neck=dict(in_channels=[512])))
