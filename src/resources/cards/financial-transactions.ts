// File generated from our OpenAPI spec by Stainless.

import * as Core from 'meorphis-test-23/core';
import { APIResource } from 'meorphis-test-23/resource';
import * as CardsAPI from 'meorphis-test-23/resources/cards/cards';

export class FinancialTransactions extends APIResource {
  /**
   * Get the card financial transaction for the provided token.
   */
  retrieve(
    cardToken: string,
    financialTransactionToken: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CardsAPI.FinancialTransaction> {
    return this._client.get(
      `/cards/${cardToken}/financial_transactions/${financialTransactionToken}`,
      options,
    );
  }
}
