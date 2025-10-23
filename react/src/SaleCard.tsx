import type { Sale } from "./CustomerSales";
import './SaleCard.css'

interface SaleCardProps {
    sale: Sale;
}

export function SaleCard(props: SaleCardProps) {
    const { sale } = props;
    const { sale_id, created_at, completed_at, store_id, vendor_id, unique_sale_id, customer_id, currency, payment } = sale;

    return <div style={{ display: "flex", flexDirection: "row", gap: "0px" }}>
        <p>{sale_id}</p>
        <p>{created_at}</p>
        <p>{completed_at}</p>
        <p>{store_id}</p>
        <p>{vendor_id}</p>
        <p>{unique_sale_id}</p>
        <p>{customer_id}</p>
        <p>{currency}</p>
        <p>{payment}</p>
    </div>
}