import { keepPreviousData, useQuery } from "@tanstack/react-query";
import { useState } from "react";
import { useParams } from "react-router";
import { SaleCard } from "./SaleCard";

export interface Sale {
    sale_id: number,
    created_at: string,
    completed_at: string,
    store_id: number,
    vendor_id: number,
    unique_sale_id: string,
    customer_id: number,
    currency: string,
    payment: string,
    billing_address: number,
    shipping_address: number,
    resource_id: number,
    guests_number: number,
    takeaway: number,
    pickup_date: string,
    sale_ext_ref: string,
    total: string,
}

interface SalesListResponse {
    sales: Sale[],
    count: number,
    page: number,
    last_page: boolean,
}

export function CustomerSales() {
    const { customer_id } = useParams();
    const [page, setPage] = useState(0);
    const { isLoading, isError, error, data } = useQuery<SalesListResponse>({
        queryKey: ['customer_sales', customer_id, page],
        queryFn: async () => {
            const res = await fetch(`http://127.0.0.1:8000/sales/customer/${customer_id}?page=${page}`, { mode: "cors" });
            if (!res.ok) throw new Error("Network response was not ok");
            return res.json();
        }, placeholderData: keepPreviousData
    });
    if (isLoading) {
        return <div>Loading...</div>;
    }
    if (error) {
        return <div>Error: {error.message}</div>;
    }
    return <>
        <div style={{ display: "flex", flexDirection: "column", gap: "0px", justifyContent: "center", alignItems: "center" }}>
            <div style={{ display: "flex", flexDirection: "row", gap: "0px" }}>
                <p>Sale ID</p>
                <p>Created at</p>
                <p>Completed at</p>
                <p>Store ID</p>
                <p>Vendor ID</p>
                <p>Unique sale ID</p>
                <p>Customer ID</p>
                <p>Currency</p>
                <p>Payment</p>
            </div>
            {data?.sales.map((sale) => (
                <SaleCard key={sale.sale_id} sale={sale} />
            ))}
        </div>
        {page > 0 && (<button onClick={() => setPage((page) => page - 1)}>Page précédente</button >)}
        {!data?.last_page && <button onClick={() => setPage((page) => page + 1)}>Page suivante</button >}
    </>
}
