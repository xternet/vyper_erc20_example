#!/usr/bin/python3
from brownie import Token, accounts

def main():
	accounts[0].deploy(Tokenx, "Token", "TKN", 18, 1000)