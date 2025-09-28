#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
모델 파일 다운로드 스크립트
필요한 모델 파일들을 자동으로 다운로드합니다.
"""

import os
import requests
from pathlib import Path

def download_file(url: str, filepath: str):
    """파일을 다운로드합니다."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    print(f"다운로드 중: {url}")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    print(f"완료: {filepath}")

def main():
    """모델 파일들을 다운로드합니다."""
    
    # 모델 다운로드 링크들 (실제 링크로 교체 필요)
    models = {
        # YOLO 모델들
        "process/model/seg.pt": "https://example.com/seg.pt",
        "process/model/detect6.pt": "https://example.com/detect6.pt",
        "process/model/0818.pt": "https://example.com/0818.pt",
        
        # LoRA 가중치들 (주요 몇 개만)
        "process/lora/7000.safetensors": "https://example.com/7000.safetensors",
        "process/lora/pome2000.safetensors": "https://example.com/pome2000.safetensors",
        "process/lora/poo1000.safetensors": "https://example.com/poo1000.safetensors",
        
        # FAISS 인덱스들
        "process/CLIP/dog_index_img.faiss": "https://example.com/dog_index_img.faiss",
        "process/CLIP/dog_ids_img.npy": "https://example.com/dog_ids_img.npy",
        "process/CLIP/dog_colors_lab.npy": "https://example.com/dog_colors_lab.npy",
        "process/CLIP/dog_breeds.npy": "https://example.com/dog_breeds.npy",
    }
    
    print("모델 파일 다운로드를 시작합니다...")
    print("주의: 실제 다운로드 링크는 README.md를 참조하세요.")
    
    for filepath, url in models.items():
        if not os.path.exists(filepath):
            try:
                download_file(url, filepath)
            except Exception as e:
                print(f"다운로드 실패: {filepath} - {e}")
        else:
            print(f"이미 존재: {filepath}")
    
    print("다운로드 완료!")

if __name__ == "__main__":
    main()
