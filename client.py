import os
import requests
from errors import build_api_error

class GlassnodeClient:

    BASE_API_URI = 'https://api.glassnode.com'
    API_VERSION = 'v1'

    def __init__(self, api_key, base_api_uri=None, api_version=None):
        if not api_key:
            raise ValueError('Missing `api_key`.')
        self.API_KEY = api_key
        self.BASE_API_URI = base_api_uri or self.BASE_API_URI
        self.API_VERSION = api_version or self.API_VERSION

    def _create_api_uri(self, subpath):
        """Internal helper for creating endpoint URIs."""
        return ''.join([self.BASE_API_URI, '/', self.API_VERSION, '/', subpath])

    def _request(self, subpath, query_parameters):
        """Internal helper for creating HTTP requests to the Glassnode API.
        Raises an APIError if the response is not 20X. Otherwise, returns the
        response object.
        """
        uri = self._create_api_uri(subpath) + '?'
        for key, value in query_parameters.items():
            uri += key + '=' + value + '&'
        uri += 'api_key=' + self.API_KEY
        response = requests.get(uri)
        return self._handle_response(response)

    def _handle_response(self, response):
        """Internal helper for handling API responses from the Glassnode server.
        Raises the appropriate exceptions when necessary; otherwise, returns the
        response.
        """
        if not str(response.status_code).startswith('2'):
            raise build_api_error(response)
        return response

    # Assets API
    # -----------------------------------------------------------
    def get_asssets(self):
        return self._request('metrics/assets', {})

    # Indicators API
    # -----------------------------------------------------------
    def get_indicator(self, indicator, query_parameters):
        return self._request('metrics/indicators/' + indicator, query_parameters)

    def get_nvt_ratio_indicator(self, query_parameters):
        return self.get_indicator('nvt', query_parameters)

    def get_coin_days_destroyed_indicator(self, query_parameters):
        return self.get_indicator('cdd', query_parameters)

    def get_average_coin_dormacy_indicator(self, query_parameters):
        return self.get_indicator('average_dormancy', query_parameters)

    def get_average_dormancy_supply_adjusted_indicator(self, query_parameters):
        return self.get_indicator('average_dormancy_supply_adjusted', query_parameters)

    def get_liveliness_indicator(self, query_parameters):
        return self.get_indicator('liveliness', query_parameters)

    def get_asol_indicator(self, query_parameters):
        return self.get_indicator('asol', query_parameters)

    def get_msol_indicator(self, query_parameters):
        return self.get_indicator('msol', query_parameters)

    # Market API
    # -----------------------------------------------------------
    def get_market(self, market, query_parameters):
        return self._request('metrics/market/' + market, query_parameters)

    def get_market_cap_realized(self, query_parameters):
        return self.get_market('marketcap_realized_usd', query_parameters)

    def get_market_value_to_realized_value(self, query_parameters):
        return self.get_market('mvrv', query_parameters)

    # Addresses API
    # -----------------------------------------------------------
    def get_address_metric(self, address_metric, query_parameters):
        return self._request('metrics/addresses/' + address_metric, query_parameters)

    def get_addresses_total_count(self, query_parameters):
        return self.get_address_metric('count', query_parameters)

    def get_addresses_active_count(self, query_parameters):
        return self.get_address_metric('active_count', query_parameters)

    def get_addresses_new_count(self, query_parameters):
        return self.get_address_metric('new_non_zero_count', query_parameters)

    def get_addresses_sending_count(self, query_parameters):
        return self.get_address_metric('sending_count', query_parameters)

    def get_addresses_receiving_count(self, query_parameters):
        return self.get_address_metric('receiving_count', query_parameters)

    # Exchanges & Transactions API
    # -----------------------------------------------------------
    def get_transaction_metric(self, transaction_metric, query_parameters):
        return self._request('metrics/transactions/' + transaction_metric, query_parameters)

    def get_exchange_inflow(self, query_parameters):
        return self.get_transaction_metric('transfers_volume_to_exchanges_sum', query_parameters)

    def get_exchange_outflow(self, query_parameters):
        return self.get_transaction_metric('transfers_volume_from_exchanges_sum', query_parameters)

    def get_exchange_deposits(self, query_parameters):
        return self.get_transaction_metric('transfers_to_exchanges_count', query_parameters)

    def get_exchange_withdrawals(self, query_parameters):
        return self.get_transaction_metric('transfers_from_exchanges_count', query_parameters)

    def get_transaction_count(self, query_parameters):
        return self.get_transaction_metric('count', query_parameters)

    def get_transaction_rate(self, query_parameters):
        return self.get_transaction_metric('rate', query_parameters)

    def get_transfer_count(self, query_parameters):
        return self.get_transaction_metric('transfers_count', query_parameters)

    def get_transfer_rate(self, query_parameters):
        return self.get_transaction_metric('transfers_rate', query_parameters)

    def get_transfer_volume_sum(self, query_parameters):
        return self.get_transaction_metric('transfers_volume_sum', query_parameters)

    def get_transfer_volume_mean(self, query_parameters):
        return self.get_transaction_metric('transfers_volume_mean', query_parameters)

    def get_transfer_volume_median(self, query_parameters):
        return self.get_transaction_metric('transfers_volume_median', query_parameters)

    def get_transfer_volume_adjusted_sum(self, query_parameters):
        return self.get_transaction_metric('transfers_volume_adjusted_sum', query_parameters)

    def get_transfer_volume_adjusted_mean(self, query_parameters):
        return self.get_transaction_metric('transfers_volume_adjusted_mean', query_parameters)

    def get_transfer_volume_adjusted_median(self, query_parameters):
        return self.get_transaction_metric('transfers_volume_adjusted_median', query_parameters)

    # Fees API
    # -----------------------------------------------------------
    def get_fee_metric(self, fee_metric, query_parameters):
        return self._request('metrics/fees/' + fee_metric, query_parameters)

    def get_fee_volume_total(self, query_parameters):
        return self.get_fee_metric('volume_sum', query_parameters)

    def get_fee_volume_mean(self, query_parameters):
        return self.get_fee_metric('volume_mean', query_parameters)

    def get_gas_used_sum(self, query_parameters):
        return self.get_fee_metric('gas_used_sum', query_parameters)

    def get_gas_used_mean(self, query_parameters):
        return self.get_fee_metric('gas_used_mean', query_parameters)

    def get_gas_used_median(self, query_parameters):
        return self.get_fee_metric('gas_used_median', query_parameters)

    def get_gas_price_mean(self, query_parameters):
        return self.get_fee_metric('gas_price_mean', query_parameters)

    def get_gas_price_median(self, query_parameters):
        return self.get_fee_metric('gas_price_median', query_parameters)

    def get_transaction_gas_limit_mean(self, query_parameters):
        return self.get_fee_metric('gas_limit_tx_mean', query_parameters)

    def get_transaction_gas_limit_median(self, query_parameters):
        return self.get_fee_metric('gas_limit_tx_median', query_parameters)


    # UTXO API
    # -----------------------------------------------------------
    def get_blockchain_metric(self, blockchain_metric, query_parameters):
        return self._request('metrics/blockchain/' + blockchain_metric, query_parameters)

    def get_utxo_created_count(self, query_parameters):
        return self.get_blockchain_metric('utxo_created_count', query_parameters)

    def get_utxo_spent_count(self, query_parameters):
        return self.get_blockchain_metric('utxo_spent_count', query_parameters)

    def get_utxo_created_value_sum(self, query_parameters):
        return self.get_blockchain_metric('utxo_created_value_sum', query_parameters)

    def get_utxo_created_value_mean(self, query_parameters):
        return self.get_blockchain_metric('utxo_created_value_mean', query_parameters)

    def get_utxo_created_value_median(self, query_parameters):
        return self.get_blockchain_metric('utxo_created_value_median', query_parameters)

    def get_utxo_spent_value_sum(self, query_parameters):
        return self.get_blockchain_metric('utxo_spent_value_sum', query_parameters)

    def get_utxo_spent_value_mean(self, query_parameters):
        return self.get_blockchain_metric('utxo_spent_value_mean', query_parameters)

    def get_utxo_spent_value_median(self, query_parameters):
        return self.get_blockchain_metric('utxo_spent_value_median', query_parameters)

    # Get Exchange Flow API
    # -----------------------------------------------------------
    def get_exchange_flow_per_ticker(self, asset, query_parameters):
        return self._request('flow/assets/' + asset + '/tickers', query_parameters)
