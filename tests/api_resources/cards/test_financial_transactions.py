# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_30 import MeorphisTest30, AsyncMeorphisTest30
from meorphis_test_30.types.cards import FinancialTransaction

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFinancialTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MeorphisTest30) -> None:
        financial_transaction = client.cards.financial_transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MeorphisTest30) -> None:
        response = client.cards.financial_transactions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = response.parse()
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MeorphisTest30) -> None:
        with client.cards.financial_transactions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = response.parse()
            assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MeorphisTest30) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.financial_transactions.with_raw_response.retrieve(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                card_token="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_transaction_token` but received ''"
        ):
            client.cards.financial_transactions.with_raw_response.retrieve(
                "",
                card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncFinancialTransactions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMeorphisTest30) -> None:
        financial_transaction = await async_client.cards.financial_transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMeorphisTest30) -> None:
        response = await async_client.cards.financial_transactions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = await response.parse()
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMeorphisTest30) -> None:
        async with async_client.cards.financial_transactions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = await response.parse()
            assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMeorphisTest30) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.financial_transactions.with_raw_response.retrieve(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                card_token="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_transaction_token` but received ''"
        ):
            await async_client.cards.financial_transactions.with_raw_response.retrieve(
                "",
                card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
