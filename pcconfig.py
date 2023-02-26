import pynecone as pc

config = pc.Config(
    app_name="pynecone_supabase_notes_app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
