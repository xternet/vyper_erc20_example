#!/usr/bin/python3
from brownie import Token, accounts

acct = accounts.load('1')

def main():
	acct.deploy(Token, "Token", "TKN", 18, 1000)