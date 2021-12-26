###===--- MesiSols NFT Minter ---===###

###===--- Imports ---===###

### General ###
import os, glob
from replit import db
import requests
import json
from generator.sol_gen import gen_sol
from image_maker.image import gen_image
from image_maker.json import gen_json

### Algo API ###
from natsort import natsorted
from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn
from minting.algo_utils import wait_for_confirmation, print_created_asset


###===--- Minting ---===###

# Set the paths for the images and metadata
images_path = 'image_maker/star_pngs'
meta_path = 'image_maker/star_json'

# Set the Pinata keys for IPFS
api_key = os.environ['pinata_k']
api_secret = os.environ['pinata_s']
acc_mnemonic = os.environ['mesi_mnemonic']

# Going to be using several print statements for debugging/performance
def mint_collection(count):
  '''
  This function runs the mint function in a loop, minting each NFT.
  
  Inputs:
    count (int): specifies how many MesiSols to mint
  
  Returns: a minted collection of MesiSols on Algorand.
  '''

  # Assert that there are enough image files to create the amount
  # of MesiSols that is desired.
  assert len(os.listdir('image_maker/star_pngs/')) >= count

  # Use a for loop to mint each NFT
  for code in range(1, count + 1):
    star = gen_sol()
    gen_json(star, code)
    gen_image(star, code)

    mint(code)


def mint(code, testnet=False):
  '''
  This function mints MesiSols to the mainnet.

  Inputs:
    count (int): specifies how many MesiSols to mint.
  '''

  ### Configuration ###

  # Find the attribute metadata of the star
  meta_file = open(f'image_maker/star_json/MesiSolsMetadata{code}.json', 'r')
  meta_dict = json.load(meta_file)
  json_meta = json.dumps(meta_dict)

  # For debugging and minting purposes, convert the code int to str.
  str_code = str(code)

  print(f'--- Initializing creation of MesiSol #{str_code} ---')

  # Using Pinata link the image to an ipfs URL for upload.
  # Do some sorting in the image path to get the right files
  imgs = natsorted(glob.glob(os.path.join(images_path, "*.png")))
  files = [('file', (str_code + ".png", open(imgs[code], "rb"))),]
  ipfs_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

  headers = {
        "pinata_api_key": api_key,
        "pinata_secret_api_key": api_secret
        }

  response: requests.Response = requests.post(url=ipfs_url, files=files, headers=headers)
  meta = response.json()

  # Sets the ipfs_cid hash
  ipfs_cid = meta['IpfsHash']

  ### Initizializing Blockchain Connection ###

  # Set the accounts for minting, setup using a dict because
  # multiple may be needed as the maximum amount of assets one
  # account can make is 1000.
  accounts = {}
  acc_counter = 1

  for m in [acc_mnemonic]:
    accounts[acc_counter] = {}
    accounts[acc_counter]['pk'] = mnemonic.to_public_key(m)
    accounts[acc_counter]['sk'] = mnemonic.to_private_key(m)
    acc_counter += 1

  # Check for Test Net and connect to client
  if testnet:
    algod_address = "https://api.testnet.algoexplorer.io"
  else:
    algod_address = "https://api.algoexplorer.io"
  
  algod_token = ""
  headers = {'User-Agent': 'py-algorand-sdk'}
  algod_client = algod.AlgodClient(algod_token, algod_address, headers);    
  status = algod_client.status()

  # Create the asset and build the transaction for the mint.
  params = algod_client.suggested_params()
  params.fee = 1000
  params.flat_fee = True

  txn = AssetConfigTxn(
    sender = accounts[1]['pk'],
    sp = params,
    total = 1,
    default_frozen = False,
    asset_name = f'MesiSol #{str_code}',
    unit_name = f'MSOL{str_code}',
    manager = accounts[1]['pk'],
    reserve = accounts[1]['pk'],
    freeze = None,
    clawback = None,
    strict_empty_address_check=False,
    url = f'ipfs://{ipfs_cid}',
    metadata_hash = '',
    note = json_meta.encode(),
    decimals = 0)
    
  # Sign the transaction using the secret key for the account and 
  # send it to the network gathering the transaction id.
  stxn = txn.sign(accounts[1]['sk'])

  txid = algod_client.send_transaction(stxn)
  print(f'--- {txid} is your transaction ID for MesiSol #{str_code} ---')

  wait_for_confirmation(algod_client, txid)

  try:
    # Pull successful transaction info.
    ptx = algod_client.pending_transaction_info(txid)
    asset_id = ptx["asset-index"]
    db[str_code] = asset_id
    print_created_asset(algod_client, accounts[1]['pk'], asset_id)
  except Exception as e:
    print(e)


