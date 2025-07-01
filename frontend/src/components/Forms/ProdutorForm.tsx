import React, { useState, useEffect } from 'react';
import { useForm, useFieldArray, useWatch } from 'react-hook-form';
import styled from 'styled-components';
import { ProdutorCreate, FazendaCreate, CulturaCreate } from '@/types';
import { validateCPFCNPJ, formatCPFCNPJ, validateAreas } from '@/utils/validation';
import toast from 'react-hot-toast';

const FormContainer = styled.div`
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 0 auto;
`;

const FormTitle = styled.h2`
  color: #333;
  margin-bottom: 2rem;
  text-align: center;
`;

const FormGroup = styled.div`
  margin-bottom: 1.5rem;
`;

const Label = styled.label`
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #333;
`;

const Input = styled.input`
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  
  &:focus {
    outline: none;
    border-color: #4caf50;
    box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.2);
  }
  
  &.error {
    border-color: #f44336;
  }
`;

const ErrorMessage = styled.span`
  color: #f44336;
  font-size: 0.875rem;
  margin-top: 0.25rem;
  display: block;
`;

const Button = styled.button`
  background: #4caf50;
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s;
  
  &:hover {
    background: #45a049;
  }
  
  &:disabled {
    background: #ccc;
    cursor: not-allowed;
  }
`;

const ButtonGroup = styled.div`
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
`;

const Section = styled.div`
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 1rem;
  margin-bottom: 1rem;
`;

const SectionTitle = styled.h3`
  color: #333;
  margin-bottom: 1rem;
`;

const AddButton = styled.button`
  background: #2196f3;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  font-size: 0.875rem;
  cursor: pointer;
  margin-bottom: 1rem;
  
  &:hover {
    background: #1976d2;
  }
`;

const RemoveButton = styled.button`
  background: #f44336;
  color: white;
  padding: 0.25rem 0.5rem;
  border: none;
  border-radius: 4px;
  font-size: 0.75rem;
  cursor: pointer;
  
  &:hover {
    background: #d32f2f;
  }
`;

interface ProdutorFormProps {
  onSubmit: (data: ProdutorCreate) => void;
  loading?: boolean;
  defaultValues?: ProdutorCreate;
}

const ProdutorForm: React.FC<ProdutorFormProps> = ({ onSubmit, loading = false, defaultValues }) => {
  const [cpfError, setCpfError] = useState<string>('');

  const {
    register,
    handleSubmit,
    control,
    watch,
    formState: { errors },
    reset,
  } = useForm<ProdutorCreate>({
    defaultValues: defaultValues || { fazendas: [] },
  });

  useEffect(() => {
    if (defaultValues) {
      reset(defaultValues);
    }
  }, [defaultValues, reset]);

  const { fields: fazendaFields, append: appendFazenda, remove: removeFazenda } = useFieldArray({
    control,
    name: 'fazendas',
  });

  const { fields: culturaFields, append: appendCultura, remove: removeCultura } = useFieldArray({
    control,
    name: 'fazendas.0.culturas',
  });

  const handleCpfCnpjChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    const formatted = formatCPFCNPJ(value);
    e.target.value = formatted;
    
    if (value.length > 0 && !validateCPFCNPJ(value)) {
      setCpfError('CPF/CNPJ inválido');
    } else {
      setCpfError('');
    }
  };

  const handleAreaValidation = (fazendaIndex: number) => {
    const fazenda = useWatch({
      control,
      name: `fazendas.${fazendaIndex}`
    });
    if (fazenda) {
      const { area_total, area_agricultavel, area_vegetacao } = fazenda;
      if (area_total && area_agricultavel && area_vegetacao) {
        if (!validateAreas(area_total, area_agricultavel, area_vegetacao)) {
          toast.error('A soma das áreas agricultável e vegetação não pode ultrapassar a área total');
        }
      }
    }
  };

  const onFormSubmit = (data: ProdutorCreate) => {
    if (cpfError) {
      toast.error('Por favor, corrija o CPF/CNPJ');
      return;
    }
    onSubmit(data);
  };

  const addFazenda = () => {
    appendFazenda({
      nome: '',
      cidade: '',
      estado: '',
      area_total: 0,
      area_agricultavel: 0,
      area_vegetacao: 0,
      culturas: [],
    });
  };

  const addCultura = () => {
    appendCultura({
      nome: '',
      safra: '',
    });
  };

  // Detecta modo edição
  const isEdit = !!defaultValues;

  return (
    <FormContainer>
      <FormTitle>{isEdit ? 'Atualizar Produtor' : 'Cadastrar Novo Produtor'}</FormTitle>
      <form onSubmit={handleSubmit(onFormSubmit)}>
        <FormGroup>
          <Label>CPF/CNPJ *</Label>
          <Input
            {...register('cpf_cnpj', { required: 'CPF/CNPJ é obrigatório' })}
            onChange={handleCpfCnpjChange}
            placeholder="000.000.000-00 ou 00.000.000/0000-00"
            className={cpfError ? 'error' : ''}
            disabled={isEdit} // Não permitir editar CPF/CNPJ
          />
          {errors.cpf_cnpj && <ErrorMessage>{errors.cpf_cnpj.message}</ErrorMessage>}
          {cpfError && <ErrorMessage>{cpfError}</ErrorMessage>}
        </FormGroup>

        <FormGroup>
          <Label>Nome do Produtor *</Label>
          <Input
            {...register('nome', { required: 'Nome é obrigatório' })}
            placeholder="Nome completo do produtor"
          />
          {errors.nome && <ErrorMessage>{errors.nome.message}</ErrorMessage>}
        </FormGroup>

        <Section>
          <SectionTitle>Fazendas</SectionTitle>
          <AddButton type="button" onClick={addFazenda}>
            + Adicionar Fazenda
          </AddButton>

          {fazendaFields.map((field, fazendaIndex) => (
            <Section key={field.id}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                <h4>Fazenda {fazendaIndex + 1}</h4>
                <RemoveButton type="button" onClick={() => removeFazenda(fazendaIndex)}>
                  Remover
                </RemoveButton>
              </div>

              <FormGroup>
                <Label>Nome da Fazenda *</Label>
                <Input
                  {...register(`fazendas.${fazendaIndex}.nome` as const, { required: 'Nome da fazenda é obrigatório' })}
                  placeholder="Nome da propriedade"
                />
              </FormGroup>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                <FormGroup>
                  <Label>Cidade *</Label>
                  <Input
                    {...register(`fazendas.${fazendaIndex}.cidade` as const, { required: 'Cidade é obrigatória' })}
                    placeholder="Cidade"
                  />
                </FormGroup>

                <FormGroup>
                  <Label>Estado *</Label>
                  <Input
                    {...register(`fazendas.${fazendaIndex}.estado` as const, { required: 'Estado é obrigatório' })}
                    placeholder="UF"
                  />
                </FormGroup>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1rem' }}>
                <FormGroup>
                  <Label>Área Total (ha) *</Label>
                  <Input
                    type="number"
                    step="0.01"
                    {...register(`fazendas.${fazendaIndex}.area_total` as const, { 
                      required: 'Área total é obrigatória',
                      min: { value: 0, message: 'Área deve ser maior que zero' }
                    })}
                    onBlur={() => handleAreaValidation(fazendaIndex)}
                  />
                </FormGroup>

                <FormGroup>
                  <Label>Área Agricultável (ha) *</Label>
                  <Input
                    type="number"
                    step="0.01"
                    {...register(`fazendas.${fazendaIndex}.area_agricultavel` as const, { 
                      required: 'Área agricultável é obrigatória',
                      min: { value: 0, message: 'Área deve ser maior que zero' }
                    })}
                    onBlur={() => handleAreaValidation(fazendaIndex)}
                  />
                </FormGroup>

                <FormGroup>
                  <Label>Área de Vegetação (ha) *</Label>
                  <Input
                    type="number"
                    step="0.01"
                    {...register(`fazendas.${fazendaIndex}.area_vegetacao` as const, { 
                      required: 'Área de vegetação é obrigatória',
                      min: { value: 0, message: 'Área deve ser maior que zero' }
                    })}
                    onBlur={() => handleAreaValidation(fazendaIndex)}
                  />
                </FormGroup>
              </div>

              <Section>
                <h5>Culturas</h5>
                <AddButton type="button" onClick={addCultura}>
                  + Adicionar Cultura
                </AddButton>

                {culturaFields.map((culturaField, culturaIndex) => (
                  <div key={culturaField.id} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr auto', gap: '1rem', alignItems: 'end', marginBottom: '1rem' }}>
                    <FormGroup>
                      <Label>Nome da Cultura</Label>
                      <Input
                        {...register(`fazendas.${fazendaIndex}.culturas.${culturaIndex}.nome` as const)}
                        placeholder="Ex: Soja, Milho"
                      />
                    </FormGroup>

                    <FormGroup>
                      <Label>Safra</Label>
                      <Input
                        {...register(`fazendas.${fazendaIndex}.culturas.${culturaIndex}.safra` as const)}
                        placeholder="Ex: 2023"
                      />
                    </FormGroup>

                    <RemoveButton type="button" onClick={() => removeCultura(culturaIndex)}>
                      Remover
                    </RemoveButton>
                  </div>
                ))}
              </Section>
            </Section>
          ))}
        </Section>

        <ButtonGroup>
          <Button type="button" onClick={() => reset(defaultValues || { fazendas: [] })}>
            Limpar
          </Button>
          <Button type="submit" disabled={loading}>
            {loading ? (isEdit ? 'Salvando...' : 'Salvando...') : isEdit ? 'Atualizar Produtor' : 'Salvar Produtor'}
          </Button>
        </ButtonGroup>
      </form>
    </FormContainer>
  );
};

export default ProdutorForm; 