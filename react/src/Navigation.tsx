import { Link } from "react-router";

export function Navigation() {
    return (
        <div style={{ flexFlow: "row nowrap", justifyContent: "space-around", gap: "1rem" }}>
            <Link to="/" style={{ fontSize: "14px", fontWeight: "500", color: "#6b7280", textDecoration: "none" }}>
                Accueil
            </Link>
        </div>
    )
}