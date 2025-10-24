import { useMutation } from "@tanstack/react-query";
import { useState } from "react";
import { Link } from "react-router";

interface SignupRequest {
    username: string,
    password: string,
}

const sendCreds = async (signupRequest: SignupRequest) => {
    const response = await fetch("http://127.0.0.1:8000/auth", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(signupRequest)
    })
    return response.json()
}


export function Signup() {
    const { isSuccess, isPending, isError, error, mutate } = useMutation({ mutationFn: sendCreds });
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        mutate({ username, password })
    }
    return <div>
        {isPending ? (
            'Création du compte...'
        ) : (
            <>
                {isError ? (
                    <div>Erreur : {error.message}</div>
                ) : null}

                {isSuccess ? <div>Compte créé !</div> : null}
                <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column" }}>
                    <span>
                        <label htmlFor="username">Nom d'utilisateur : </label>
                        <input id="username" name="username" type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                    </span>
                    <span>
                        <label htmlFor="password">Mot de passe : </label>
                        <input id="password" name="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                    </span>
                    <button type="submit">Envoyer</button>
                </form>
            </>)}
        <Link to={`/login`}>Se connecter</Link>
    </div>
}