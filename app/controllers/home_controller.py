from flask import Blueprint, jsonify

def home():
    return jsonify("Endpoint test OK"), 200