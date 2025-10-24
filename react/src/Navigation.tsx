import { Link } from "react-router";

export function Navigation() {
    return (
        <div style={{ display: "flex", gap: "1rem", justifyContent: "center" }}>
            <Link to="/">Accueil</Link>
            <Link to="/customers">Customers</Link>
            <Link to="/login">Login</Link>
        </div>
    )
}