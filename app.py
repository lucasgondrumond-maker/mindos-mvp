if user_input := st.chat_input("Digite sua mensagem aqui..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("MINDOS está pensando..."):
            result = graph.invoke({"objective": user_input})
            
            # Extrai o texto da chave "response"
            if isinstance(result, dict) and "response" in result:
                resposta = result["response"]
            else:
                resposta = str(result)
                
            st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})
