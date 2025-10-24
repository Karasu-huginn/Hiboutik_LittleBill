import { useQuery } from "@tanstack/react-query";
import { useState } from "react";
import { Link } from "react-router";

interface Customer {
    customers_id: number,
    last_name: string,
    first_name: string,
    email: string,
    phone: string,
    vat: string,
    country: string,
    date_of_birth: string,
    validity: string,
    loyalty_points: number,
    intial_loyalty_points: number,
    prepaid_purchases: string,
    store_credit: string,
    customers_ref_ext: string,
    last_order_date: string,
    customers_code: string,
}

interface CustomerListResponse {
    customers: Customer[];
    count: number;
}

export function CustomerSearch() {
    const [email, setEmail] = useState("");
    const [last_name, setLastName] = useState("");
    const { isLoading, isError, error, data, refetch } = useQuery<CustomerListResponse>({
        queryKey: ['customer', email, last_name],
        queryFn: async () => {
            const res = await fetch(`http://127.0.0.1:8000/customer/search?last_name=${last_name}&email=${email}`, {
                mode: "cors", headers: {
                    'Authorization': localStorage.getItem("token") || ""
                }
            });
            if (!res.ok) throw new Error("Network response was not ok");
            return res.json();
        },
        enabled: false,
        staleTime: 1000 * 60 * 5,
    });

    const handleSearch = (e: React.FormEvent) => {
        e.preventDefault()
        refetch();
    }
    return <>
        <form onSubmit={handleSearch} style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
            <span>
                <label htmlFor="last_name">Nom du client : </label>
                <input id="last_name" name="last_name" type="text" placeholder="Nom de famille..." value={last_name} onChange={(e) => setLastName(e.target.value)} />
            </span>
            <span>
                <label htmlFor="email">Email du client : </label>
                <input id="email" name="email" type="text" placeholder="Email..." value={email} onChange={(e) => setEmail(e.target.value)} />
            </span>
            <button type="submit">Rechercher</button>
        </form>

        {isLoading && <div>Chargement...</div>}
        {isError && <div>Erreur : {(error as Error).message}</div>}
        {data && (
            <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "1rem" }}>
                {data.count > 0 ? (
                    data.customers.map((result) => (
                        <Link key={result.customers_id} to={`/customer-sales/${result.customers_id}`}>
                            <div style={{ border: "1px solid #ccc", padding: "1rem" }}>
                                <h2>{result.last_name} {result.first_name}</h2>
                                <p>Email : {result.email}</p>
                                <p>Pays : {result.country}</p>
                            </div>
                        </Link>
                    ))
                ) : (
                    <h3>Aucun résultat trouvé. Essayez d'ajuster vos critères de recherche.</h3>
                )}
            </div>
        )}
    </>
}