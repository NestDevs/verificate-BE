from web3 import Web3
import json
from src.config.settings import settings


# Opening JSON file
async def provider():
   verificate_abi = json.load(open('src/web3/abi/verificate.json'))
   provider = Web3.HTTPProvider(settings.INFURAL_URL)
   web3 = Web3(provider)
   web3.isConnected()
   contract_address = web3.toChecksumAddress(settings.CONTRACT_ADDRESS)
   deployed_contract = web3.eth.contract(address=contract_address, abi=verificate_abi)
   
   return {"connected":web3.isConnected(),"web3":web3, "deployed_contract":deployed_contract}


# Mint certificate
async def mint_certificate(user_address,certificate_hash):
    """
        Mint a certificate for a user
        :param user_id: id of user to mint certificate for
        :return: {
            "success":True,
            "message":"Certificate minted successfully",
            "tx_hash":tx_hash,
            "tx_receipt":tx_receipt,
            "status":201
        } if successful
        :return: {
            "success":False,
            "message":"Certificate could not be minted",
            "status":500
        } if certificate could not be minted
    """
    try:
        # mint certificate
        _provider = await provider()
        if _provider["connected"]:
            contract = _provider["deployed_contract"]
            #Build trancsaction
            owner_account = settings.OWNER_ACCOUNT
            private_key=settings.OWNER_ACCOUNT_PRIVATE_KEY
            #get the nonce.  Prevents one from sending the transaction twice
            nonce = _provider["web3"].eth.getTransactionCount(owner_account)
            mint_certificate = contract.functions.safeMint(user_address,certificate_hash).buildTransaction(
                {
                    'from': owner_account,
                    'nonce': nonce,
                    'gas': 1000000,
                    'gasPrice': _provider["web3"].toWei("70", "gwei"),

                }
            )

            signed_txn = _provider["web3"].eth.account.sign_transaction(mint_certificate, 
            private_key=private_key)
            tx_hash = _provider["web3"].eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_receipt = _provider["web3"].eth.waitForTransactionReceipt(tx_hash)
            if tx_receipt is not None:
                return {
                    "success":True,
                    "message":"Certificate minted successfully",
                    "tx_hash":tx_hash,
                    "tx_receipt":tx_receipt,
                    "status":201
                    }
            else:
                return {
                    "success":False,
                    "message":"Certificate could not be minted",
                    "status":500
                    }
        else:
            return {
                "success":False,
                "message":"Provider is not connected",
                "status":500
                }

    except Exception as error:
        return {
            "success":False,
            "message":"An error occurred while minting the certificate : " + str(error),
            "status":500
            }


