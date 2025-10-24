import { useMutation } from "@tanstack/react-query";
import { useState } from "react";
import { Link } from "react-router";

interface LoginRequest {
    username: string,
    password: string,
}

const sendCreds = async (loginRequest: LoginRequest) => {
    const response = await fetch("http://127.0.0.1:8000/auth/token", {
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        },
        body: new URLSearchParams({
            'username': loginRequest.username,
            'password': loginRequest.password
        })
    })
    return response.json()
}

export function Login() {
    const { isSuccess, isPending, isError, error, mutate, data } = useMutation({ mutationFn: sendCreds });
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        mutate({ username, password })
    }
    if (isSuccess) {
        localStorage.setItem("token", `${data.token_type} ${data.access_token}`)
    }
    return <div>
        {isPending ? (
            'Connexion...'
        ) : (
            <>
                {isError ? (
                    <div>Erreur : {error.message}</div>
                ) : null}

                {isSuccess ? <div>Connecté !</div> : null}
                <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column" }}>
                    <span>
                        <label htmlFor="username">Nom d'utilisateur : </label>
                        <input id="username" name="username" type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                    </span>
                    <span>
                        <label htmlFor="password">Mot de passe : </label>
                        <input id="password" name="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                    </span>
                    <button type="submit">Se connecter</button>
                </form>
            </>)}
        <Link to={`/signup`}>Créer un compte</Link>
    </div>
}