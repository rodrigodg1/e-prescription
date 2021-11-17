#!/bin/bash


rm -rf prescription-files/*
rm -rf encrypted-prescription-files/*
rm -rf binary_enc_prescription/*
rm -rf binary_enc_to_cipher_prescription/*


rm -rf separate-prescription-data/ENCRYPTED*
rm -rf separate-prescription-data/medication/medication*
rm -rf separate-prescription-data/medication/encrypted/*

rm -rf separate-prescription-data/personal_ID/patient*
rm -rf separate-prescription-data/personal_ID/encrypted/*


rm -rf separate-prescription-data/diagnosis/diagnosis*
rm -rf separate-prescription-data/diagnosis/encrypted/*


rm -rf separate-prescription-data/encrypted_diagnosis_size_in_bytes
rm -rf separate-prescription-data/encrypted_medication_size_in_bytes
rm -rf separate-prescription-data/encrypted_personal_ID_size_in_bytes


rm -rf report/CLEAR*
rm -rf report/ENCRYPTED*
rm -rf report/memory-evaluation/*
rm -rf report/execution-time-evaluation/*
rm -rf report/prescription_size_encrypted_in_bytes
rm -rf report/prescription_size_clear_text_in_bytes
rm -rf report/prescription_size_encrypted_binary_in_bytes


##